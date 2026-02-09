from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404,
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]

    bag = request.session.get("bag", {})
    item_id = str(item_id)

    # If product has sizes, size is required
    if product.has_sizes:
        if not size:
            messages.error(request, "Please select a size.")
            return redirect(redirect_url)

        # Ensure item structure exists
        if item_id in bag:
            if "items_by_size" not in bag[item_id]:
                bag[item_id] = {"items_by_size": {}}

            if size in bag[item_id]["items_by_size"]:
                bag[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to '
                    f'{bag[item_id]["items_by_size"][size]}'
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

    # No sizes
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


def adjust_bag(request, item_id):
    """ Adjust the quantity of the spec prod to specified amount """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get("quantity"))

    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]

    bag = request.session.get("bag", {})
    item_id = str(item_id)

    if product.has_sizes:
        if not size:
            messages.error(request, "Please select a size.")
            return redirect(reverse("view_bag"))

        # Ensure item structure exists
        if item_id in bag and "items_by_size" not in bag[item_id]:
            bag[item_id] = {"items_by_size": {}}

        if quantity > 0:
            bag[item_id]["items_by_size"][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to '
                f'{bag[item_id]["items_by_size"][size]}'
            )
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)

            messages.success(
                request,
                f"Removed size {size.upper()} {product.name} from your bag"
            )

    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f"Updated {product.name} quantity to {bag[item_id]}"
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                f"Removed {product.name} from your bag"
            )

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    try:
        size = None
        if "product_size" in request.POST:
            size = request.POST["product_size"]

        bag = request.session.get("bag", {})
        item_id = str(item_id)

        if product.has_sizes:
            if not size:
                return HttpResponse(status=400)

            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)

            messages.success(
                request,
                f"Removed size {size.upper()} {product.name} from your bag"
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                f"Removed {product.name} from your bag"
            )

        request.session["bag"] = bag
        return redirect(reverse("view_bag"))

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return redirect(reverse("view_bag"))
