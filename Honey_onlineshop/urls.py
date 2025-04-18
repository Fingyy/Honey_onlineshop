"""
URL configuration for Honey_onlineshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from shop.models import (Honey, HoneyProductOnStock, DeliveryAndPay, Packaging)
from shop.views import (BaseView, AboutUsView, HoneyListView, HoneyDetailView, HoneyCreateView, HoneyDeleteView,
                        HoneyUpdateView, HoneyProductOnStockCreateView, HoneyProductOnStockListView,
                        HoneyProductOnStockUpdateView, HoneyProductOnStockDeleteView,
                        PackagingCreateView, PackingUpdateView, PackagingDeleteView)

admin.site.register([Honey, HoneyProductOnStock, DeliveryAndPay, Packaging])

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('o-nas/', AboutUsView.as_view(), name='about_us'),
    path('admin/', admin.site.urls),
    path('medy/', HoneyListView.as_view(), name='honey_list'),
    path('medy/<int:pk>/', HoneyDetailView.as_view(), name='honey_detail'),
    path('medy/vytvorit/', HoneyCreateView.as_view(), name='honey_create'),
    path('medy/smazat/<int:pk>', HoneyDeleteView.as_view(), name='honey_delete'),
    path('medy/update/<int:pk>', HoneyUpdateView.as_view(), name='honey_update'),
    path('sklad/seznam/', HoneyProductOnStockListView.as_view(), name='stock_prod_list'),
    path('sklad/vytvorit/', HoneyProductOnStockCreateView.as_view(), name='stock_prod_create'),
    path('sklad/update/<int:pk>', HoneyProductOnStockUpdateView.as_view(), name='stock_prod_update'),
    path('sklad/smazat/<int:pk>', HoneyProductOnStockDeleteView.as_view(), name='stock_prod_delete'),
    path('baleni/vytvorit/', PackagingCreateView.as_view(), name='packaging_create'),
    path('baleni/smazat/<pk>', PackagingDeleteView.as_view(), name='packaging_delete'),
    path('baleni/update/<int>:pk', PackingUpdateView.as_view(), name='packaging_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
