from django.contrib import admin
from django.urls import include, path
# from rest_framework import routers
# from ecommerce import views

urlpatterns = [
    path('', include('ecommerce.urls'))
    # path('admin/', admin.site.urls),       
    # path('api/', include(router.urls)),
]

# router = routers.DefaultRouter()

# router.register(r'supplier', views.SupplierView, 'supplier')
# router.register(r'product', views.ProductView, 'product')
# router.register(r'client', views.ClientView, 'client')
# router.register(r'invoice', views.InvoiceView, 'invoice')



