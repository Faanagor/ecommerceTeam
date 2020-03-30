from rest_framework import viewsets
from .serializers import SupplierSerializer, ProductSerializer, ClientSerializer, InvoiceSerializer
from .models import Supplier, Product, Client, Invoice