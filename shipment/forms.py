from django import forms
from .models import Company, Type, Invoice, ProductDetail, BankDetails, Shipment, StatusUpdate

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'post_code', 'type', 'contact_info', 'website']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['company', 'invoice_number', 'invoice_date', 'invoice_status', 'proforma_invoice',
                  'date_issued', 'type', 'quantity', 'gross', 'net', 'price_per_kg', 'payment_to',
                  'amount', 'location']

class ProductDetailForm(forms.ModelForm):
    class Meta:
        model = ProductDetail
        fields = ['invoice', 'grade', 'number_of_packages', 'gross_weight', 'net_weight', 'price_per_kg', 'amount']

class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = ['company', 'bank_name', 'bank_address', 'account_number', 'account_name', 'swift', 'iban', 'reference_number']

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['tracking_number', 'estimated_arrival', 'actual_arrival', 'waybill_number', 'shipping_company',
                  'current_location', 'invoice', 'total_amount']

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = StatusUpdate
        fields = ['shipment', 'status', 'updated_by', 'comments']
