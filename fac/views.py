from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

from bases.views import SinPrivilegios
from fac.models import Cliente, FacturaEnc, FacturaDet

from .forms import ClienteForm

# Create your views here.
class ClienteView(SinPrivilegios, ListView):
    model = Cliente
    template_name = 'fac/clientes_list.html'
    context_object_name = 'obj'
    permission_required = 'fac.view_cliente'

class VistaBaseCreate(SuccessMessageMixin, SinPrivilegios, CreateView):
    context_object_name = 'obj'
    success_message = 'Registro agregado satisfactoriamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, UpdateView):
    context_object_name = 'obj'
    success_message = 'Registro actualizado satisfactoriamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ClienteNew(VistaBaseCreate):
    model = Cliente
    template_name = 'fac/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('fac_app:clientes_list')
    permission_required = 'fac.add_cliente'

class ClienteEdit(VistaBaseEdit):
    model = Cliente
    template_name = 'fac/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('fac_app:clientes_list')
    permission_required = 'fac.change_cliente'


@login_required(login_url="/login/")
@permission_required("fac.change_cliente", login_url="/login/")
def inactivarCliente(request, id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method=='POST':
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    return HttpResponse("FAIL")

class FacturaView(SinPrivilegios, ListView):
    model = FacturaEnc
    template_name = 'fac/factura_list.html'
    context_object_name = 'obj'
    permission_required = 'fac.view_facturaenc'