from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ["order_history", "product", "quantity"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "created_at"]
    inlines = (OrderItemInline,)
    readonly_fields = ["created_at"]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["product", "created_at"]
    readonly_fields = ["created_at"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
