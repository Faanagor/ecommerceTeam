from django.http import HttpResponse

from rest_framework import viewsets, permissions
from .serializers import SupplierSerializer, ProductSerializer, ClientSerializer, InvoiceSerializer
from .models import Supplier, Product, Client, Invoice

class SupplierViewSet(viewsets.ModelViewSet):
	serializer_class = SupplierSerializer
	queryset = Supplier.objects.all() 
	permissions_classes = [
		permissions.AllowAny
	]

	#   def perform_create(self, serializer):
	#         author = get_object_or_404(Author, id=self.request.data.get('author_id'))
	#         return serializer.save(author=author)

	#     def get(self, request, *args, **kwargs):
	#         return self.list(request, *args, *kwargs)

	#     def post(self, request, *args, **kwargs):
	#         return self.create(request, *args, **kwargs)

class ProductViewSet(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
	permissions_classes = [
		permissions.AllowAny
	]
  
class ClientViewSet(viewsets.ModelViewSet):
	serializer_class = ClientSerializer
	queryset = Client.objects.all()
	permissions_classes = [
		permissions.AllowAny
	]

class InvoiceViewSet(viewsets.ModelViewSet):
	serializer_class = InvoiceSerializer
	queryset = Invoice.objects.all()
	permissions_classes = [
		permissions.AllowAny
	]

# def index(request):
#     return HttpResponse("Hello, world. You're at the ecommerce index.")