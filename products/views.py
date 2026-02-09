from django.shortcuts import render
from .models import Product, Category


def product_list(request):
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    # FILTER: category
    if "category" in request.GET:
        category = request.GET.get("category")
        if category:
            products = products.filter(category__name=category)
            categories = Category.objects.filter(name=category)

    # SORT: price / rating / category
    if "sort" in request.GET:
        sort = request.GET.get("sort")

        if sort == "category":
            sortkey = "category__name"
        else:
            sortkey = sort

        # Optional direction
        direction = request.GET.get("direction")
        if direction == "desc":
            sortkey = f"-{sortkey}"

        products = products.order_by(sortkey)

    context = {
        "products": products,
        "current_categories": categories,
        "current_sorting": f"{sort}_{direction}",
    }

    return render(request, "products/product_list.html", context)
