"""ecommerceTeam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from ecommerce import views

# router = routers.DefaultRouter()
# router.register(r'supplier', views.SupplierView, 'ecommerce')
# router.register(r'product', views.ProductView, 'ecommerce')
# router.register(r'client', views.ClientView, 'ecommerce')
# router.register(r'invoice', views.InvoiceView, 'ecommerce')

router = routers.DefaultRouter()

router.register(r'supplier', views.SupplierView, 'supplier')
router.register(r'product', views.ProductView, 'product')
router.register(r'client', views.ClientView, 'client')
router.register(r'invoice', views.InvoiceView, 'invoice')


urlpatterns = [
    path('admin/', admin.site.urls),       
    path('api/', include(router.urls)),
]
