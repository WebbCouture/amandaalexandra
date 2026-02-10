import stripe

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from bag.contexts import bag_contents
from .forms import OrderForm


def checkout(request):
    bag = request.session.get("bag", {})

    # Stoppa tom checkout
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse("products"))

    # Stripe PaymentIntent
    stripe.api_key = settings.STRIPE_SECRET_KEY

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
