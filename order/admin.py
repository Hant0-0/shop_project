from django.contrib import admin

from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'create', 'update', 'paid']
    list_filter = ['create', 'update', 'paid']
    inlines = [OrderItemInline, ]


admin.site.register(Order, OrderAdmin)
