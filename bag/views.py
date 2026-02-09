from django.shortcuts import render


def view_bag(request):
    """Show shopping bag page"""
    return render(request, "bag/bag.html")
