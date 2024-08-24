from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import uuid

from django.utils import timezone

class Company(models.Model):
    SHIPPING = 'Shipping'
    BANK = 'Bank'
    OTHER = 'Other'

    COMPANY_TYPE_CHOICES = [
        (SHIPPING, 'Shipping'),
        (BANK, 'Bank'),
        (OTHER, 'Other'),
    ]

    address = models.TextField(blank=True, null=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, choices=COMPANY_TYPE_CHOICES, default=OTHER, blank=True, null=True)
    contact_info = models.TextField(null=True, blank=True)
    website = models.URLField(_("Website"), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(_("Product Name"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

class Invoice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
    invoice_date = models.DateField(_("Invoice Date"), blank=True, null=True)
    invoice_status = models.CharField(max_length=50, blank=True, null=True)
    proforma_invoice = models.CharField(max_length=20, blank=True, null=True, unique=True)
    date_issued = models.DateField(null=True, blank=True)
    
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(_("Number of Pkgs"), blank=True, null=True)
    gross = models.FloatField(_("Kilos - Gross"), blank=True, null=True)
    net = models.FloatField(_("Kilos - NET"), blank=True, null=True)
    price_per_kg = models.IntegerField(_("Price Per KG"), blank=True, null=True)
    payment_to = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    location = models.CharField(_("Location"), max_length=100, blank=True, null=True, help_text='CIF Alex Old Port')

    def __str__(self):
        return self.invoice_number

class ProductDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='product_details')
    grade = models.CharField(max_length=50, blank=True, null=True)
    number_of_packages = models.IntegerField(blank=True, null=True)
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.grade} - {self.invoice.invoice_number}"

class BankDetails(models.Model):
    company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE, related_name='bank_details')
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_address = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(_("Account Number"), max_length=50, blank=True, null=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    swift = models.CharField(_("Swift"), max_length=20, blank=True, null=True)
    iban = models.CharField(_("IBAN"), max_length=50, blank=True, null=True)
    reference_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("BankDetails")
        verbose_name_plural = _("Bank Details")

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"

class Shipment(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    estimated_arrival = models.DateField(blank=True, null=True)
    actual_arrival = models.DateField(blank=True, null=True)
    waybill_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    shipping_company = models.CharField(max_length=255, blank=True, null=True)
    current_location = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='shipments', blank=True, null=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.tracking_number

    def generate_tracking_number(self):
     
        return str(uuid.uuid4()).replace("-", "").upper()[:12]  

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = self.generate_tracking_number()
        super(Shipment, self).save(*args, **kwargs)
class StatusUpdate(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.status
