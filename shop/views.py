from django.shortcuts import render
from shop.models import Category, Product


def product_list(request):
    category = Category.objects.all()
    product = Product.objects.filter(available=True)

    return render(request, 'shop/list.html', {'category': category, 'product': product})


