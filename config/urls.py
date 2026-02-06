from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # Allauth authentication URLs
    path('accounts/', include('allauth.urls')),

    # Homepage
    path('', include('products.urls')),
]
