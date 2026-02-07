from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Allauth
    path('accounts/', include('allauth.urls')),

    # Home page
    path('', include('home.urls')),
]
