from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Supplier
from .models import Product
from .models import Client
from .models import Invoice
        
class PostView(viewsets.ModelViewSet):
  serializer_class = PostSerializer
  querysetSupplier = Supplier.objects.all()
  querysetProduct = Product.objects.all()
  querysetClient = Client.objects.all()
  querysetInvoice = Invoice.objects.all()

# def index(request):
#     return HttpResponse("Hello, world. You're at the ecommerce index.")