from django.urls import path
from . import views
from . import webhooks

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path(
        "checkout_success/<str:order_number>/",
        views.checkout_success,
        name="checkout_success",
    ),
    path(
        "order_history/<str:order_number>/",
        views.order_history,
        name="order_history",
    ),
    path("wh/", webhooks.webhook, name="webhook"),
]
