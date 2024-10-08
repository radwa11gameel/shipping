# Generated by Django 5.0.6 on 2024-08-24 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='acid',
        ),
        migrations.AlterField(
            model_name='bankdetails',
            name='account_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bankdetails',
            name='account_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Account Number'),
        ),
        migrations.AlterField(
            model_name='bankdetails',
            name='bank_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bankdetails',
            name='bank_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bankdetails',
            name='iban',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='IBAN'),
        ),
        migrations.AlterField(
            model_name='bankdetails',
            name='reference_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bankdetails',
            name='swift',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Swift'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(blank=True, choices=[('Shipping', 'Shipping'), ('Bank', 'Bank'), ('Other', 'Other')], default='Other', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='location',
            field=models.CharField(blank=True, help_text='CIF Alex Old Port', max_length=100, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_to',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='proforma_invoice',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipment.type'),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='grade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='gross_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='net_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='number_of_packages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='price_per_kg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='estimated_arrival',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='shipment.invoice'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipping_company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='waybill_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='statusupdate',
            name='shipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipment.shipment'),
        ),
        migrations.AlterField(
            model_name='statusupdate',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Product Name'),
        ),
        migrations.DeleteModel(
            name='ACID',
        ),
    ]
