from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path("news/", views.news_list, name="news_list"),
    path("news/create/", views.news_create, name="news_create"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("news/<slug:slug>/edit/", views.news_edit, name="news_edit"),
    path("news/<slug:slug>/delete/", views.news_delete, name="news_delete"),
]
