from django.contrib import admin
from .models import Supplier    # import the Supplier model
from .models import Product     # import the Product model
from .models import Client      # import the Client model
from .models import Invoice     # import the Invoice model
admin.site.register(Supplier)    #this to register the Supplier model
admin.site.register(Product)    #this to register the Product model
admin.site.register(Client)    #this to register the Client model
admin.site.register(Invoice)    #this to register the Invoice model

# Register your models here.