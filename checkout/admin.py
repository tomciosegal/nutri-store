from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
	model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
	inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItemHistory)

class OrderItemHistoryInline(admin.TabularInline):
    model = OrderItemHistory
    fields = ["order_history", "product", "quantity"]
    
class OrderHistoryAdmin(admin.ModelAdmin):
    inlines = (OrderItemHistoryInline,)
    readonly_fields = ["created_at"]

admin.site.register(OrderHistory, OrderHistoryAdmin)



