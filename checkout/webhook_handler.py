from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle generic/unknown webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle successful payment intent"""
        return HttpResponse(
            content=f'Payment Intent Succeeded: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle failed payment intent"""
        return HttpResponse(
            content=f'Payment Failed: {event["type"]}',
            status=200
        )
