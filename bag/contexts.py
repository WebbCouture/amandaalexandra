from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product


def bag_contents(request):
    bag_items = []
    total = Decimal("0.00")
    product_count = 0

    bag = request.session.get("bag", {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        # Products with sizes: item_data is a dict: {"items_by_size": {...}}
        if isinstance(item_data, dict):
            for size, quantity in item_data["items_by_size"].items():
                subtotal = quantity * product.price
                total += subtotal
                product_count += quantity

                bag_items.append({
                    "item_id": item_id,
                    "quantity": quantity,
                    "product": product,
                    "size": size,
                    "subtotal": subtotal,
                })

        # Products without sizes: item_data is an int quantity
        else:
            quantity = item_data
            subtotal = quantity * product.price
            total += subtotal
            product_count += quantity

            bag_items.append({
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
                "size": None,
                "subtotal": subtotal,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal("0.00")
        free_delivery_delta = Decimal("0.00")

    grand_total = total + delivery

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
