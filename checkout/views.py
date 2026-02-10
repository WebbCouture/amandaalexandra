import stripe

from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})

    # Stoppa tom checkout
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    # Stripe PaymentIntent (test)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=1000,   # 10.00 (testbelopp)
        currency='sek',
    )

    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    return render(request, "checkout/checkout.html", context)
