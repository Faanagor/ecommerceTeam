from rest_framework import serializers
from .models import Supplier
from .models import Product
from .models import Client
from .models import Invoice
      
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        field = ('idSupplier', 'nitSupplier', 'nameSupplier', 'categorySupplier', 'telephoneSupplier', 'emailSupplier', 
        'citySupplier', 'addressSupplier', 'descriptionSupplier')

    class Meta:
        model = Product
        fields = ('idProduct', 'nameProduct', 'priceSaleProduct', 'quantityProduct', 'categoryProduct', 'descriptionProduct',
        'nameSupplierProduct', 'entryDateProduct', 'expirationDateProduct', 'pricePurchaseProduct', 'utilityProduct')

    class Meta:
        model = Client
        field = ('idClient', 'numberClient', 'nameClient', 'lastNameClient', 'cityClient', 'addressClient', 'telephoneClient',
        'emailClient')

    class Meta:
        model = Invoice
        field = ('idInvoice', 'dateInvoice', 'TotalPriceInvoice', 'nameClientInvoice', 'lastNameClientInvoice', 'productsInvoice',
        'nameProductsInvoice', 'employeeInvoice',)