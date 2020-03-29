from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import SupplierSerializer, ProductSerializer, ClientSerializer, InvoiceSerializer
from .models import Supplier, Product, Client, Invoice
        
class SupplierView(viewsets.ModelViewSet):
  serializer_class = SupplierSerializer
  queryset = Supplier.objects.all()
  
class ProductView(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  
class ClientView(viewsets.ModelViewSet):
  serializer_class = ClientSerializer
  queryset = Client.objects.all()

class InvoiceView(viewsets.ModelViewSet):
  serializer_class = InvoiceSerializer
  queryset = Invoice.objects.all()

# def index(request):
#     return HttpResponse("Hello, world. You're at the ecommerce index.")