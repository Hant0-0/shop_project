from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=category)
    return render(request, 'shop/list.html', {'categories': categories, 'product': product, 'category': category})

def product_detail(request):
    categories = Category.objects.all()
    return render(request, 'shop/detail.html', {'categories': categories})




