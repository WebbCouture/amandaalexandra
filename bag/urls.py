from django.urls import path
from . import views   # ✅ rätt import

urlpatterns = [
    path("", views.view_bag, name="view_bag"),
]
