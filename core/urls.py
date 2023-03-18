from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list')
]
