from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.views import ProductAPIList, ProductAPIDetail, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'api-category', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),

    # ------------ API -------------------
    path('', include(router.urls)),
    path('api-product/', ProductAPIList.as_view()),
    path('api-product/<int:pk>/', ProductAPIDetail.as_view()),

    path('', include('shop.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)