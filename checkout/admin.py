from django.contrib import admin
from .models import OrderItemHistory, OrderHistory


admin.site.register(OrderItemHistory)

class OrderItemHistoryInline(admin.TabularInline):
    model = OrderItemHistory
    fields = ["order_history", "product", "quantity"]
    
class OrderHistoryAdmin(admin.ModelAdmin):
    inlines = (OrderItemHistoryInline,)
    readonly_fields = ["created_at"]

admin.site.register(OrderHistory, OrderHistoryAdmin)

 

