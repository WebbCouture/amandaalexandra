from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category


def product_list(request):
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None
    query = None

    # SEARCH: q
    if "q" in request.GET:
        query = request.GET.get("q")
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse("product_list"))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    # FILTER: category (supports comma-separated)
    if "category" in request.GET:
        category = request.GET.get("category")
        if category:
            category_list = category.split(",")
            products = products.filter(category__name__in=category_list)
            categories = Category.objects.filter(name__in=category_list)

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
        "search_term": query,
    }

    return render(request, "products/product_list.html", context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
