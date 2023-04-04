from django.shortcuts import render, redirect, get_object_or_404

from cart.cart import Cart
from order.forms import OrderForm
from order.models import Order
from shop.models import Product


def order(request):
    cart = Cart(request)
    if request.method == 'GET':
        orders = OrderForm()
        return render(request, 'order/order_detail.html', {'orders': orders, 'cart': cart})
    else:
        orders = OrderForm(request.POST)
        if orders.is_valid():
            orders.save()
            cart.clear()
        return render(request, 'order/order_created.html')


