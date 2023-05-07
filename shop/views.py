from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.forms import CartAddProductForms
from shop.models import Category, Product
from django.db.models import Q

from shop.serializers import CategorySerializer, ProductSerializer


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        multi_q = Q(Q(name__icontains=q) | Q(description__icontains=q))
        product = Product.objects.filter(multi_q, available=True)
    else:
        product = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=category)
    return render(request, 'shop/list.html', {'categories': categories, 'product': product, 'category': category})


def product_detail(request, pr_id, product_slug):
    products = get_object_or_404(Product, id=pr_id, slug=product_slug)
    cart_product_form = CartAddProductForms()
    return render(request, 'shop/detail.html', {'products': products, 'cart_product_form': cart_product_form})


# --------------  CREATE API -----------------------

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductAPIList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

