import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from bases.views import SinPrivilegios
from cmp.forms import ProveedorForm, CompraEncForm
from cmp.models import Proveedor, ComprasEnc, ComprasDet
from inv.models import Producto


class ProveedorView(SinPrivilegios, ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    permission_required = 'cmp.view_comprasenc'

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

def proveedor_inactivar_modal(request, id):
    prov = Proveedor.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'cmp/inactivar_modal.html'

    if not prov:
        return HttpResponse('Proveedor no existe: '+str(id))

    if request.method=='GET':
        contexto = {'obj': prov}

    if request.method=='POST':
        prov.estado = False
        prov.save()
        contexto = {'obj':'OK'}
        return HttpResponse('Proveedor inactivado')

    return render(request, template_name, contexto)

class ComprasView(SinPrivilegios, ListView):
    model = ComprasEnc
    template_name = 'cmp/compras_list.html'
    context_object_name = 'obj'
    permission_required = 'cmp.view_comprasenc'

@login_required(login_url='/login/')
@permission_required('cmp.view_comprasenc', login_url='bases_app:sin_privilegios')
def compras(request, compra_id=None):
    template_name = 'cmp/compras.html'
    prod = Producto.objects.filter(estado=True)
    form_compras = {}
    contexto = {}

    if request.method == 'GET':
        form_compras = CompraEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            
            e = {
                'fecha_compra': fecha_compra,
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'nro_factura': enc.nro_factura,
                'fecha_factura': fecha_factura,
                'subtotal': enc.subtotal,
                'descuento': enc.descuento,
                'total': enc.total
            }
            form_compras = CompraEncForm(e)
        else:
            det = None

        contexto = {
            'productos': prod,
            'encabezado': enc,
            'detalle': det,
            'form_enc': form_compras
        }

    if request.method == 'POST':
        fecha_compra = request.POST.get('fecha_compra')
        observacion = request.POST.get('observacion')
        nro_factura = request.POST.get('nro_factura')
        fecha_factura = request.POST.get('fecha_factura')
        proveedor = request.POST.get('proveedor')
        subtotal = 0
        descuento = 0
        total = 0

        if not compra_id:
            prov = Proveedor.objects.get(pk=proveedor)

            enc = ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                nro_factura=nro_factura,
                fecha_factura=fecha_factura,
                proveedor=prov,
                uc=request.user
            )
            if enc:
                enc.save()
                compra_id = enc.id
        else:
            enc = ComprasEnc.objects.filter(pk=compra_id).first()

            if enc:
                enc.fecha_compra = fecha_compra
                enc.observacion = observacion
                enc.nro_factura = nro_factura
                enc.fecha_factura = fecha_factura
                enc.um = request.user.id
                enc.save()

        if not compra_id:
            return redirect('cmp_app:compras_list')

        producto = request.POST.get('id_id_producto')
        cantidad = request.POST.get('id_cantidad_detalle')
        precio = request.POST.get('id_precio_detalle')
        sub_total_detalle = request.POST.get('id_sub_total_detalle')
        descuento_detalle = request.POST.get('id_descuento_detalle')
        total_detalle = request.POST.get('id_total_detalle')

        prod = Producto.objects.get(pk=producto)

        det = ComprasDet(
            compra=enc,
            producto=prod,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            costo=0,
            uc=request.user
        )

        if det:
            det.save()

            sub_total = ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('subtotal'))
            descuento = ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            enc.subtotal = sub_total['subtotal__sum']
            enc.descuento = descuento['descuento__sum']
            enc.save()

        return redirect('cmp_app:compra_edit', compra_id=compra_id)

    return render(request, template_name, contexto)

class DetalleDelete(SinPrivilegios, DeleteView):
    permission_required = 'cmp.delete_comprasdet'
    model = ComprasDet
    template_name = 'cmp/detalle_delete.html'
    context_object_name = 'obj'
    
    def get_success_url(self):
        compra_id = self.kwargs['compra_id']
        return reverse_lazy('cmp_app:compra_edit', kwargs={'compra_id': compra_id})