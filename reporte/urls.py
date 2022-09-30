from django.urls import path
from cmp.reportes import reporte_compras
from .views import ReporteCompras, FacturaPDFView

app_name = 'rep_app'

urlpatterns = [
    #Proveedor
    path('compra/pdf/<int:pk>/', FacturaPDFView.as_view(), name='factura_pdf'),
]