from django.views.generic import ListView

from bases.views import SinPrivilegios
from fac.models import Cliente


# Create your views here.
class ClienteView(SinPrivilegios, ListView):
    model = Cliente
    template_name = 'fac/clientes_list.html'
    context_object_name = 'obj'
    permission_required = 'fac.view_cliente'