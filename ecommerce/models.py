from django.db import models

# Create your models here.

class Supplier(models.Model):
    # ACTIVATE_SUPPLIER = (
    #     ('Activate', 'Activo'),
    #     ('Desactivate', 'Inactivo'),
    # )
    idSupplier = models.IntegerField(primary_key= True)
    nitSupplier = models.CharField(max_length=20)
    nameSupplier = models.CharField(max_length=50)
    categorySupplier = models.CharField(max_length=50)
    telephoneSupplier = models.CharField(max_length=10)
    emailSupplier = models.CharField(max_length=80, null=True)
    citySupplier = models.CharField(max_length=50)
    addressSupplier = models.CharField(max_length=80)
    descriptionSupplier = models.CharField(max_length=300)

    # activateSupplier = models.CharField(max_length=10, choices=ACTIVATE_SUPPLIER, default= 'Activo')

class Product(models.Model):
    # ACTIVATE_PRODUCT = (
    #     ('Activate', 'Activo'),
    #     ('Desactivate', 'Inactivo'),
    # )
    idProduct = models.IntegerField(primary_key= True)
    nameProduct = models.CharField(max_length=50)
    priceSaleProduct = models.FloatField() 
    quantityProduct = models.IntegerField()
    categoryProduct = models.CharField(max_length=50)
    descriptionProduct = models.CharField(max_length=300)
    nameSupplierProduct = models.CharField(max_length=50)
    entryDateProduct = models.DateField()
    expirationDateProduct = models.DateField(null=True, blank = True)
    pricePurchaseProduct = models.FloatField()
    utilityProduct = models.FloatField()
    # activateProduct = models.CharField(max_length=10, choices=ACTIVATE_PRODUCT, default= 'Activo')

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE) # Relation 1 to many supplier-product

class Client(models.Model):
    # ACTIVATE_CLIENT = (
    #     ('Activate', 'Activo'),
    #     ('Desactivate', 'Inactivo'),
    # )
    idClient = models.IntegerField(primary_key= True)
    numberClient = models.CharField(max_length=10)
    nameClient = models.CharField(max_length=50)
    lastNameClient = models.CharField(max_length=50)
    cityClient = models.CharField(max_length=50)
    addressClient = models.CharField(max_length=80)
    telephoneClient = models.CharField(max_length=10)
    emailClient = models.CharField(max_length=80, null=True, blank = True)
    
    # activateClient = models.CharField(max_length=10, choices=ACTIVATE_CLIENT, default= 'Activo')
    products = models.ManyToManyField(Product) # Relation many to many  product-client
    
    class Meta:
        ordering = ["nameClient"]
        # verbose_name_plural = "oxen"

class Invoice(models.Model):
    # ACTIVATE_INVOICE = (
    #     ('Activate', 'Activo'),
    #     ('Desactivate', 'Inactivo'),
    # )
    idInvoice = models.IntegerField(primary_key= True)
    dateInvoice = models.DateField()
    TotalPriceInvoice = models.FloatField()
    nameClientInvoice = models.CharField(max_length=50)
    lastNameClientInvoice = models.CharField(max_length=50)
    productsInvoice = models.CharField(max_length=50)
    nameProductsInvoice = models.CharField(max_length=50)
    employeeInvoice = models.CharField(max_length=50)
    # activateInvoice = models.CharField(max_length=10, choices=ACTIVATE_INVOICE, default= 'Activo')   

    client = models.ForeignKey(Client, on_delete=models.CASCADE) # Relation 1 to many  client-invoice
    products = models.ManyToManyField(Product) # Relation many to many  product-invoice

