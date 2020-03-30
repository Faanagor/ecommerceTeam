# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from rest_framework import routers
from .views import SupplierViewSet, ProductViewSet, ClientViewSet, InvoiceViewSet

router = routers.DefaultRouter()
router.register('api/supplier', SupplierViewSet, 'supplier')
router.register('api/product', ProductViewSet, 'product')
router.register('api/client', ClientViewSet, 'client')
router.register('api/invoice', InvoiceViewSet, 'invoice')

urlpatterns = router.urls


# router = routers.DefaultRouter()

# router.register(r'supplier', views.SupplierView, 'supplier')
# router.register(r'product', views.ProductView, 'product')
# router.register(r'client', views.ClientView, 'client')
# router.register(r'invoice', views.InvoiceView, 'invoice')


# urlpatterns = [
#     path('', include('ecommerce.urls')),
#     path('admin/', admin.site.urls),       
#     path('api/', include(router.urls)),
# ]
