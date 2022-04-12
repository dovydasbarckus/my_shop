from django.contrib import admin
from .models import Customer, Order, Product, ProductOrder, Status

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", 'f_name', 'l_name', 'email')
    list_filter = ('f_name', 'l_name',)
    search_fields = ('f_name', 'l_name', 'email')
    list_editable = ('f_name', 'l_name', 'email')


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 0 # išjungia placeholder'ius


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_id','user', 'status_id', 'date_ordered')
    inlines = [ProductOrderInline]

    fieldsets = (
        ('Availability', {
            'fields': ('customer_id', 'user', 'status_id', 'date_ordered')
        }),
    )


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'order_id', 'quantity')
    list_editable = ('quantity',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_editable = ('price',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
admin.site.register(Status)