from django.shortcuts import render

from cart.cart import Cart


def cart(request):
    return {'cart': Cart(request)}