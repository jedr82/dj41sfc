from django.urls import path
from cmp.views import *

app_name = 'cmp_app'

urlpatterns = [
    #Proveedor
    path('proveedores/', ProveedorView.as_view(), name='proveedores_list'),
    path('proveedor/add/', ProveedorNew.as_view(), name='proveedor_add'),
    path('proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>', proveedor_inactivar, name='proveedor_inactivar'),
]