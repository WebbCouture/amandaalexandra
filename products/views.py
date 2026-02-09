from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

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

    # SORT: price / rating / category / name
    if "sort" in request.GET:
        sortkey = request.GET.get("sort")
        sort = sortkey

        # Case-insensitive sorting for name
        if sortkey == "name":
            products = products.annotate(lower_name=Lower("name"))
            sortkey = "lower_name"

        # Category sorting (by name, not id)
        if sortkey == "category":
            sortkey = "category__name"

        direction = request.GET.get("direction")
        if direction == "desc":
            sortkey = f"-{sortkey}"

        products = products.order_by(sortkey)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "current_categories": categories,
        "current_sorting": current_sorting,
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
