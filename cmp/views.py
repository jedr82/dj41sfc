from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from cmp.forms import ProveedorForm
from cmp.models import Proveedor
from inv.models import Producto


# Create your views here.
class ProveedorView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    login_url = 'bases_app:login'

class ProveedorNew(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp_app:proveedores_list')
    login_url = 'bases_app:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, UpdateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp_app:proveedores_list')
    login_url = 'bases_app:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def proveedor_inactivar(request, id):
    proveedor = Proveedor.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'cmp/inactivar.html'

    if not proveedor:
        return redirect('cmp_app:proveedores_list')

    if request.method == 'GET':
        contexto = {'obj': proveedor}

    if request.method == 'POST':
        proveedor.estado = False
        proveedor.save()
        return redirect('cmp_app:proveedores_list')

    return render(request, template_name, contexto)