from rest_framework import serializers
from .models import Company, Invoice, Type, Shipment, StatusUpdate, ProductDetail, BankDetails

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'



class InvoiceSerializer(serializers.ModelSerializer):
    shipments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
 
    invoice = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProductDetail
        fields = '__all__'


class ShipmentSerializer(serializers.ModelSerializer):
    invoice = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Shipment
        fields = '__all__'


class StatusUpdateSerializer(serializers.ModelSerializer):
    shipment = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = StatusUpdate
        fields = '__all__'


class BankDetailsSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = BankDetails
        fields = '__all__'
