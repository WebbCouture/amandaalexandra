from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import NewsArticleForm
from .models import NewsArticle


def index(request):
    return render(request, "home/index.html")


def news_list(request):
    articles = NewsArticle.objects.all()
    if not request.user.is_superuser:
        articles = articles.filter(is_published=True)

    return render(request, "home/news_list.html", {"articles": articles})


def news_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)
    if not article.is_published and not request.user.is_superuser:
        raise Http404

    return render(request, "home/news_detail.html", {"article": article})


@login_required
def news_create(request):
    if not request.user.is_superuser:
        raise Http404

    if request.method == "POST":
        form = NewsArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "News article created.")
            return redirect(reverse("news_list"))
        messages.error(request, "Please correct the errors below.")
    else:
        form = NewsArticleForm()

    return render(request, "home/news_form.html", {"form": form, "is_edit": False})


@login_required
def news_edit(request, slug):
    if not request.user.is_superuser:
        raise Http404

    article = get_object_or_404(NewsArticle, slug=slug)

    if request.method == "POST":
        form = NewsArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "News article updated.")
            return redirect(reverse("news_detail", args=[article.slug]))
        messages.error(request, "Please correct the errors below.")
    else:
        form = NewsArticleForm(instance=article)

    return render(
        request,
        "home/news_form.html",
        {"form": form, "is_edit": True, "article": article},
    )


@login_required
def news_delete(request, slug):
    if not request.user.is_superuser:
        raise Http404

    article = get_object_or_404(NewsArticle, slug=slug)

    if request.method == "POST":
        article.delete()
        messages.success(request, "News article deleted.")
        return redirect(reverse("news_list"))

    return render(request, "home/news_confirm_delete.html", {"article": article})
