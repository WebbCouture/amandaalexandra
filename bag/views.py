from django.shortcuts import render, redirect, get_object_or_404
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
    size = request.POST.get("product_size")  # will be None if not provided

    bag = request.session.get("bag", {})

    item_id = str(item_id)

    if product.has_sizes:
        if item_id in bag:
            if size in bag[item_id]["items_by_size"]:
                bag[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    f"Updated size {size.upper()} {product.name} quantity "
                    f"to {bag[item_id]['items_by_size'][size]}"
                )
            else:
                bag[item_id]["items_by_size"][size] = quantity
                messages.success(
                    request,
                    f"Added size {size.upper()} {product.name} to your bag"
                )
        else:
            bag[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request,
                f"Added size {size.upper()} {product.name} to your bag"
            )
    else:
        if item_id in bag:
            bag[item_id] += quantity
            messages.success(
                request,
                f"Updated {product.name} quantity to {bag[item_id]}"
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request,
                f"Added {product.name} to your bag"
            )

    request.session["bag"] = bag
    return redirect(redirect_url)
