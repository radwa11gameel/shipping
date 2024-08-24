from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import all_data_view, CompanyViewSet, InvoiceViewSet, ShipmentViewSet, StatusUpdateViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'shipments', ShipmentViewSet)
router.register(r'statusupdates', StatusUpdateViewSet)

from django.urls import path
from .api import all_data_view, download_pdf, enter_data

urlpatterns = [
    path('api/', include(router.urls)),
    path('data/', all_data_view, name='temp'),
    path('download-pdf/', download_pdf, name='download_pdf'),
    path('data-entry/', enter_data, name='data-entry'),
]
