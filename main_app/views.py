from django.db.models.aggregates import Sum
from django.shortcuts import render,redirect
from django.contrib import messages
from main_app.models import CartItems, Item

def menu_list(request):
    all_items = Item.objects.filter(created_by = request.user)
    context = {"all_items":all_items}
    return render(request, 'main/menu_list.html', context)

def item_detail(request, slug):
    item = Item.objects.get(slug=slug)
    context = {"item":item}
    return render(request, 'main/item_detail.html', context)

def add_to_cart(request, slug):
    item = Item.objects.get(slug=slug)
    cart_items = CartItems.objects.create(
        item = item,
        user = request.user, 
        status = "Active"
    )

    messages.success(request, "Item Added To Cart...Continue Shopping!!")
    return redirect('main:menu-list')

def get_cart_items(request):
    cart_items = CartItems.objects.filter(user=request.user)
    bill = cart_items.aggregate(Sum('item__price'))
    number = cart_items.aggregate(Sum('quantity'))
    pieces = cart_items.aggregate(Sum('item__pieces'))
    total = bill.get('item__price__sum')
    count = number.get('quantity__sum')
    total_pieces = pieces.get('item__pieces__sum')
    context = {
        "cart_items": cart_items,
        "total_bill":total,
        "count": count,
        "total_pieces": total_pieces
    }
    return render(request, 'main/cart.html',context)

def remove_cart_item(request, item_id):
    cart_item = CartItems.objects.get(pk = item_id)
    cart_item.delete()
    return redirect('main:cart')
