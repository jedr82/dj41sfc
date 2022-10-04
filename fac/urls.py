from django.urls import path, include

from fac.views import ClienteView, ClienteNew, ClienteEdit

app_name = 'fac_app'

urlpatterns = [
    path('clientes/', ClienteView.as_view(), name='clientes_list'),
    path('cliente/new', ClienteNew.as_view(), name='cliente_add'),
    path('cliente/edit/<int:pk>', ClienteEdit.as_view(), name='cliente_edit'),
]