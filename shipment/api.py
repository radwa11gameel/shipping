from rest_framework import viewsets,permissions
from .models import Company, Type, Invoice, ProductDetail, BankDetails, Shipment, StatusUpdate
from .serializers import CompanySerializer, InvoiceSerializer, ShipmentSerializer,  StatusUpdateSerializer, ProductDetailSerializer, TypeSerializer, BankDetailsSerializer
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .forms import CompanyForm, TypeForm, InvoiceForm, ProductDetailForm,  BankDetailsForm, ShipmentForm, StatusUpdateForm


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class BankDetailsViewSet(viewsets.ModelViewSet):
    queryset = BankDetails.objects.all()
    serializer_class = BankDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class StatusUpdateViewSet(viewsets.ModelViewSet):
    queryset = StatusUpdate.objects.all()
    serializer_class = StatusUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

def all_data_view(request):
    context = {
        'companies': Company.objects.all(),
        'types': Type.objects.all(),
        'invoices': Invoice.objects.all(),
        'product_details': ProductDetail.objects.all(),
        'bank_details': BankDetails.objects.all(),
        'shipments': Shipment.objects.all(),
        'status_updates': StatusUpdate.objects.all(),
    }
   
    return render(request, 'temp.html', context)


def render_to_pdf(template_src, context_dict={}):
    template = render_to_string(template_src, context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'
    result = pisa.CreatePDF(template, dest=response)
    if result.err:
        return None
    return response

def download_pdf(request):
    context = {
            'companies': Company.objects.all(),
            'types': Type.objects.all(),
            'invoices': Invoice.objects.all(),
            'product_details': ProductDetail.objects.all(),
            'bank_details': BankDetails.objects.all(),
            'shipments': Shipment.objects.all(),
            'status_updates': StatusUpdate.objects.all(),
        }
    
    return render_to_pdf('temp.html', context)


def enter_data(request):
    if request.method == 'POST':
        if 'submit_company' in request.POST:
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                company = company_form.save()
                return redirect('data-entry')  
        else:
            company_form = CompanyForm()

        if 'submit_type' in request.POST:
            type_form = TypeForm(request.POST)
            if type_form.is_valid():
                type_form.save()
                return redirect('data-entry')
        else:
            type_form = TypeForm()

        if 'submit_invoice' in request.POST:
            invoice_form = InvoiceForm(request.POST)
            if invoice_form.is_valid():
                invoice_form.save()
                return redirect('data-entry')
        else:
            invoice_form = InvoiceForm()

        if 'submit_product_detail' in request.POST:
            product_detail_form = ProductDetailForm(request.POST)
            if product_detail_form.is_valid():
                product_detail_form.save()
                return redirect('data-entry')
        else:
            product_detail_form = ProductDetailForm()

        if 'submit_bank_details' in request.POST:
            bank_details_form = BankDetailsForm(request.POST)
            if bank_details_form.is_valid():
                bank_details_form.save()
                return redirect('data-entry')
        else:
            bank_details_form = BankDetailsForm()

        if 'submit_shipment' in request.POST:
            shipment_form = ShipmentForm(request.POST)
            if shipment_form.is_valid():
                shipment_form.save()
                return redirect('data-entry')
        else:
            shipment_form = ShipmentForm()

        if 'submit_status_update' in request.POST:
            status_update_form = StatusUpdateForm(request.POST)
            if status_update_form.is_valid():
                status_update_form.save()
                return redirect('data-entry')
        else:
            status_update_form = StatusUpdateForm()
    else:
        company_form = CompanyForm()
        type_form = TypeForm()
        invoice_form = InvoiceForm()
        product_detail_form = ProductDetailForm()
        bank_details_form = BankDetailsForm()
        shipment_form = ShipmentForm()
        status_update_form = StatusUpdateForm()

    return render(request, 'data.html', {
        'company_form': company_form,
        'Type_form': type_form,
        'invoice_form': invoice_form,
        'ProductDetail_form': product_detail_form,
        'BankDetails_form': bank_details_form,
        'shipment_form': shipment_form,
        'status_update_form': status_update_form,
    })
