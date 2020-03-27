from django.db import models

# Create your models here.

class Client(models.Model):
    idClient = models.IntegerField(max_length=10, primary_key= True)
    numberClient = models.CharField(max_length=10)
    nameClient = models.CharField(max_length=50)
    lastNameClient = models.CharField(max_length=50)
    cityClient = models.CharField(max_length=50)
    addressClient = models.CharField(max_length=80)
    telephoneClient = models.CharField(max_length=10)
    emailClient = models.CharField(max_length=80, null=True, blank = True)
    
    activateClient = models.IntegerField(max_length=10)

class Product(models.Model):
    idProduct = models.IntegerField(max_length=10, primary_key= True)
    nameProduct = models.CharField(max_length=50)
    priceSaleProduct = models.FloatField() 
    quantityProduct = models.IntegerField(max_length=10)
    categoryProduct = models.CharField(max_length=50)
    descriptionProduct = models.CharField(max_length=300)
    nameSupplierProduct = models.CharField(max_length=50)
    entryDateProduct = models.DateField()
    expirationDateProduct = models.DateField(null=True, blank = True)
    pricePurchaseProduct = models.FloatField()
    utilityProduct = models.FloatField()

    activateProduct = models.IntegerField(max_length=10)

class Supplier(models.Model):
    idSupplier = models.IntegerField(max_length=10, primary_key= True)
    nitSupplier = models.CharField(max_length=20)
    nameSupplier = models.CharField(max_length=50)
    categorySupplier = models.CharField(max_length=50)
    telephoneSupplier = models.CharField(max_length=10)
    emailSupplier = models.CharField(max_length=80, null=True)
    citySupplier = models.CharField(max_length=50)
    addressSupplier = models.CharField(max_length=80)
    descriptionSupplier = models.CharField(max_length=300)

    activateSupplier = models.IntegerField(max_length=10)

class Invoice(models.Model):
    idInvoice = models.IntegerField(primary_key= True)
    dateInvoice = models.DateField()
    TotalPriceInvoice = models.FloatField()
    nameClientInvoice = models.CharField(max_length=50)
    lastNameClientInvoice = models.CharField(max_length=50)
    productsInvoice = models.CharField(max_length=50)
    nameProductsInvoice = models.CharField(max_length=50)
    employeeInvoice = models.CharField(max_length=50)
    activateInvoice = models.BinaryField(max_length=1)    

