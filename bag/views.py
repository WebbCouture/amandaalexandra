from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """Show shopping bag page"""
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = request.POST.get("product_size")

    bag = request.session.get("bag", {})
    item_id = str(item_id)

    if product.has_sizes:
        if not size:
            messages.error(request, "Please select a size.")
            return redirect(redirect_url)

        if item_id in bag:
            # Guard for old/bad session data
            if isinstance(bag[item_id], int):
                bag[item_id] = {"items_by_size": {}}

            if "items_by_size" not in bag[item_id]:
                bag[item_id] = {"items_by_size": {}}

            if size in bag[item_id]["items_by_size"]:
                bag[item_id]["items_by_size"][size] += quantity
            else:
                bag[item_id]["items_by_size"][size] = quantity
        else:
            bag[item_id] = {"items_by_size": {size: quantity}}

    else:
        # Guard for old/bad session data
        if item_id in bag and isinstance(bag[item_id], dict):
            bag[item_id] = 0

        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product in the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = request.POST.get("product_size")

    bag = request.session.get("bag", {})
    item_id = str(item_id)

    if product.has_sizes:
        if not size:
            messages.error(request, "Please select a size.")
            return redirect(reverse("view_bag"))

        # Guard for old/bad session data
        if item_id in bag and isinstance(bag[item_id], int):
            bag[item_id] = {"items_by_size": {}}

        if item_id in bag and "items_by_size" not in bag[item_id]:
            bag[item_id] = {"items_by_size": {}}

        if quantity > 0:
            bag[item_id]["items_by_size"][size] = quantity
        else:
            if size in bag[item_id]["items_by_size"]:
                del bag[item_id]["items_by_size"][size]

            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id, None)

    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id, None)

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove the specified item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get("product_size")

        bag = request.session.get("bag", {})
        item_id = str(item_id)

        if product.has_sizes:
            if item_id in bag and "items_by_size" in bag[item_id]:
                if size in bag[item_id]["items_by_size"]:
                    del bag[item_id]["items_by_size"][size]

                if not bag[item_id]["items_by_size"]:
                    bag.pop(item_id, None)
        else:
            bag.pop(item_id, None)

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception:
        return HttpResponse(status=500)
