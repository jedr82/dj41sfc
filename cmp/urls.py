from django.urls import path
from cmp.views import *
from .reportes import reporte_compras, imprimir_compra

app_name = 'cmp_app'

urlpatterns = [
    #Proveedor
    path('proveedores/', ProveedorView.as_view(), name='proveedores_list'),
    path('proveedor/add/', ProveedorNew.as_view(), name='proveedor_add'),
    path('proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>', proveedor_inactivar, name='proveedor_inactivar'),
    path('proveedor/inactivar_modal/<int:id>', proveedor_inactivar_modal, name='proveedor_inactivar_modal'),

    # Compras
    path('compras/', ComprasView.as_view(), name='compras_list'),
    path('compras/new', compras, name='compras_new'),
    path('compra/edit/<int:compra_id>', compras, name='compra_edit'),
    path('compra/<int:compra_id>/delete/<int:pk>', DetalleDelete.as_view(), name='detalle_delete'),

    #reportes
    path('compras/listado', reporte_compras, name='compras_print_all'),
    path('compras/pdf/<int:compra_id>', imprimir_compra, name='compras_print_one'),
]