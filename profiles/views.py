from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import UserProfile


@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    orders = profile.orders.all().order_by("-date")

    context = {
        "profile": profile,
        "orders": orders,
    }

    return render(request, "profiles/profile.html", context)
