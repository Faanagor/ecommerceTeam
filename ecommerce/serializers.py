from rest_framework import serializers
from .models import Supplier, Product, Client, Invoice
      
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        field = ('idSupplier', 'nitSupplier', 'nameSupplier', 'categorySupplier', 'telephoneSupplier', 'emailSupplier', 
        'citySupplier', 'addressSupplier', 'descriptionSupplier')
        # field = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('idProduct', 'nameProduct', 'priceSaleProduct', 'quantityProduct', 'categoryProduct', 'descriptionProduct',
        'nameSupplierProduct', 'entryDateProduct', 'expirationDateProduct', 'pricePurchaseProduct', 'utilityProduct')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        field = ('idClient', 'numberClient', 'nameClient', 'lastNameClient', 'cityClient', 'addressClient', 'telephoneClient',
        'emailClient')

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        field = ('idInvoice', 'dateInvoice', 'TotalPriceInvoice', 'nameClientInvoice', 'lastNameClientInvoice', 'productsInvoice',
        'nameProductsInvoice', 'employeeInvoice',)