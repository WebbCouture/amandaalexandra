import stripe

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt

from bag.contexts import bag_contents
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem
from .webhook_handler import StripeWH_Handler


def checkout(request):
    bag = request.session.get("bag", {})

    # Stoppa tom checkout
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse("product_list"))

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)

            # Stripe PID från client_secret (kräver hidden input i templaten)
            client_secret = request.POST.get("client_secret")

            if client_secret:
                stripe_pid = client_secret.split("_secret")[0]
            else:
                stripe_pid = None

            order.stripe_pid = stripe_pid
            order.save()

            # Skapa line items från bag
            for item_id, item_data in bag.items():
                product = get_object_or_404(Product, pk=item_id)

                # Om produkten inte har size: bag[item_id] = quantity (int)
                if isinstance(item_data, int):
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                else:
                    # Om produkten har size:
                    # bag[item_id]["items_by_size"][size] = quantity
                    items_by_size = item_data.get("items_by_size", {})
                    for size, quantity in items_by_size.items():
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            product_size=size,
                            quantity=quantity,
                        )

            # Valfritt: spara info-flagga i session (används senare i kursen)
            request.session["save_info"] = "save-info" in request.POST

            return redirect(reverse("checkout_success",
                                    args=[order.order_number]))

        messages.error(
            request,
            "There was an error with your form. Please check your details.",
        )
        # Fall through -> rendera sidan igen med fel

    # GET (och även POST om form är invalid): skapa PaymentIntent
    current_bag = bag_contents(request)
    total = current_bag["grand_total"]
    stripe_total = round(total * 100)

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    context = {
        "order_form": order_form,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret,
    }

    return render(request, "checkout/checkout.html", context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(
        request,
        f"Order successfully processed! Your order number is {order_number}.",
    )

    # Töm bag efter lyckad order
    if "bag" in request.session:
        del request.session["bag"]

    return render(
        request,
        "checkout/checkout_success.html",
        {"order": order},
    )


@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WH_SECRET

    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    handler = StripeWH_Handler(request)

    # Map webhook events to handler functions
    event_map = {
        "payment_intent.succeeded": handler.handle_event,
        "payment_intent.payment_failed": handler.handle_event,
    }

    event_type = event["type"]
    event_handler = event_map.get(event_type, handler.handle_event)

    return event_handler(event)
