from django import forms
from django.utils.text import slugify

from .models import NewsArticle


class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ("title", "slug", "excerpt", "content", "is_published")

    def clean_slug(self):
        slug = self.cleaned_data.get("slug")
        title = self.cleaned_data.get("title")

        if not slug and title:
            slug = slugify(title)

        return slug
