from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from order import views

urlpatterns = [
    path('', views.order, name='order')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)