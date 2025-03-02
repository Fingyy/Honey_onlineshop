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

from shop.models import (Honey, DeliveryAndPay)
from shop.views import (BaseView, AboutUsView, HoneyListView, HoneyDetailView, HoneyCreateView, HoneyDeleteView, HoneyUpdateView)

admin.site.register([Honey, DeliveryAndPay])

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('o-nas/', AboutUsView.as_view(), name='about_us'),
    path('admin/', admin.site.urls),
    path('medy/', HoneyListView.as_view(), name='honey_list'),
    path('medy/<int:pk>/', HoneyDetailView.as_view(), name='honey_detail'),
    path('medy/vytvorit/', HoneyCreateView.as_view(), name='honey_create'),
    path('medy/smazat/<int:pk>', HoneyDeleteView.as_view(), name='honey_delete'),
    path('medy/update/<int:pk>', HoneyUpdateView.as_view(), name='honey_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
