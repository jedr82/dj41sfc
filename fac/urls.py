from django.urls import path, include

from fac.views import ClienteView

app_name = 'fac_app'

urlpatterns = [
    path('clientes/', ClienteView.as_view(), name='clientes_list'),
]
