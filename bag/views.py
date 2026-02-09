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
        # size must be provided for products with sizes
        if not size:
            messages.error(request, "Please select a size.")
            return redirect(redirect_url)

        if item_id in bag:
            # If old session data stored this item as an int, convert it
            if isinstance(bag[item_id], int):
                bag[item_id] = {"items_by_size": {}}

            # Ensure expected dict structure exists
            if "items_by_size" not in bag[item_id]:
                bag[item_id] = {"items_by_size": {}}

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
        # If old session data stored this item as dict, convert it
        if item_id in bag and isinstance(bag[item_id], dict):
            bag[item_id] = 0

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
