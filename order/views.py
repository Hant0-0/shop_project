from django.shortcuts import render, redirect

from cart.cart import Cart
from order.forms import OrderForm
from order.models import OrderItem


def order(request):
    cart = Cart(request)
    if request.method == 'GET':
        orders = OrderForm()
        return render(request, 'order/order_detail.html', {'orders': orders, 'cart': cart})
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['price'])
            cart.clear()
            return render(request, 'order/send_order.html', {'order': order})

