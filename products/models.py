from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=254)
    description = models.TextField()

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )

    # ✅ Lägg upload_to så filer hamnar i /media/products/
    image = models.ImageField(
        upload_to="products/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    # ✅ Säker URL: undviker 404 om DB pekar på fil som inte finns
    @property
    def image_safe_url(self):
        # 1) Om ImageField finns och filen existerar → använd den
        try:
            if self.image and self.image.name and self.image.storage.exists(self.image.name):
                return self.image.url
        except Exception:
            pass

        # 2) Om extern image_url finns → använd den
        if self.image_url:
            return self.image_url

        # 3) Annars → placeholder (din fil i media/products/)
        return "/media/products/placeholder.jpg"
