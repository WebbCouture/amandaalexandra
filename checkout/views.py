import stripe

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from bag.contexts import bag_contents
from products.models import Product
from profiles.models import UserProfile
from .forms import OrderForm
from .models import Order, OrderLineItem


def checkout(request):
    bag = request.session.get("bag", {})

    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse("product_list"))

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)

            if request.user.is_authenticated:
                profile, _ = UserProfile.objects.get_or_create(
                    user=request.user
                    )

                order.user_profile = profile

            client_secret = request.POST.get("client_secret")

            if client_secret:
                stripe_pid = client_secret.split("_secret")[0]
            else:
                stripe_pid = None

            order.stripe_pid = stripe_pid
            order.save()

            for item_id, item_data in bag.items():
                product = get_object_or_404(Product, pk=item_id)

                if isinstance(item_data, int):
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                else:
                    items_by_size = item_data.get("items_by_size", {})
                    for size, quantity in items_by_size.items():
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            product_size=size,
                            quantity=quantity,
                        )

            request.session["save_info"] = "save-info" in request.POST

            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )

        messages.error(
            request,
            "There was an error with your form. Please check your details.",
        )

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

    if "bag" in request.session:
        del request.session["bag"]

    return render(
        request,
        "checkout/checkout_success.html",
        {"order": order},
    )


@login_required
def order_history(request, order_number):
    order = get_object_or_404(
        Order,
        order_number=order_number,
        user_profile__user=request.user,
    )

    return render(
        request,
        "checkout/checkout_success.html",
        {"order": order, "from_profile": True},
    )
