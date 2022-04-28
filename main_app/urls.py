from django.urls import path
from main_app import views

app_name = 'main'
urlpatterns = [
    path('', views.menu_list, name='menu-list'),
    path('item-detail/<slug>', views.item_detail, name="item-detail"), 
    path('add-to-cart/<slug>', views.add_to_cart, name="add-to-cart"),
    path('cart/', views.get_cart_items, name="cart"),
    path('remove-cart-item/<item_id>', views.remove_cart_item, name="remove-cart-item")
]
