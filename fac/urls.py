from django.urls import path, include

from fac.views import ClienteView, ClienteNew, ClienteEdit, inactivarCliente,FacturaView

app_name = 'fac_app'

urlpatterns = [
    #Clientes
    path('clientes/', ClienteView.as_view(), name='clientes_list'),
    path('cliente/new', ClienteNew.as_view(), name='cliente_add'),
    path('cliente/edit/<int:pk>', ClienteEdit.as_view(), name='cliente_edit'),
    path('cliente/estado/<int:id>', inactivarCliente, name='cliente_inactivar'),

    #Facturas
    path('facturas/', FacturaView.as_view(), name='facturas_list'),
]
