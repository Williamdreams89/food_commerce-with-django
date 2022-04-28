from django.contrib import admin

from main_app.models import CartItems, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'pieces', 'created_by', 'label', 'image']


class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['item','id','quantity', 'ordered', 'status','delivery_date']
admin.site.register(Item, ItemAdmin)
admin.site.register(CartItems, CartItemsAdmin)