from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("line_total",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "paid", "created_at")
    list_filter = ("paid", "created_at")
    search_fields = ("email", "full_name")
    inlines = (OrderItemInline,)
