from django.contrib import admin
from .models import Company,  Invoice, Shipment, StatusUpdate, Type, BankDetails, ProductDetail

admin.site.register(Company)
admin.site.register(Invoice)
admin.site.register(Shipment)
admin.site.register(StatusUpdate)
admin.site.register(Type)
admin.site.register(BankDetails)
admin.site.register(ProductDetail)