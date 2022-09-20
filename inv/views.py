from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView

from inv.forms import CategoriaForm, SubCategoriaForm, MarcaForm, UniMedidaForm, ProductoForm
from inv.models import Categoria, SubCategoria, Marca, UniMedida, Producto

from bases.views import SinPrivilegios


class CategoriaView(SinPrivilegios, LoginRequiredMixin, ListView):
    permission_required = 'inv.view_categoria'
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases_app:login'

class CategoriaNew(SuccessMessageMixin,SinPrivilegios, LoginRequiredMixin, CreateView):
    permission_required = 'inv.add_categoria'
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv_app:categorias_list')
    login_url = 'bases_app:login'
    success_message = 'Nueva categoría creada correctamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(SuccessMessageMixin, SinPrivilegios, LoginRequiredMixin, UpdateView):
    permission_required = 'inv.change_categoria'
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv_app:categorias_list')
    login_url = 'bases_app:login'
    success_message = 'Categoría actualizada correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def categoria_inactivar(request, id):
    cat = Categoria.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/inactivar.html'

    if not cat:
        return redirect('inv_app:categorias_list')

    if request.method == 'GET':
        contexto = {'obj': cat}

    if request.method == 'POST':
        cat.estado = False
        cat.save()
        messages.error(request, 'Categoria inactivada')
        return redirect('inv_app:categorias_list')

    return render(request, template_name, contexto)

class SubCategoriaView(SinPrivilegios, LoginRequiredMixin, ListView):
    permission_required = 'inv.view_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases_app:login'

class SubCategoriaNew(SinPrivilegios, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    permission_required = 'inv.add_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv_app:subcategorias_list')
    login_url = 'bases_app:login'
    success_message = 'Nueva subcategoría creada correctamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(SinPrivilegios, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'inv.change_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv_app:subcategorias_list')
    login_url = 'bases_app:login'
    success_message = 'SubCategoría actualizada correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def subcategoria_inactivar(request, id):
    subcat = SubCategoria.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/inactivar.html'

    if not subcat:
        return redirect('inv_app:subcategorias_list')

    if request.method == 'GET':
        contexto = {'obj': subcat}

    if request.method == 'POST':
        subcat.estado = False
        subcat.save()
        messages.error(request, 'SubCategoria inactivada')
        return redirect('inv_app:subcategorias_list')

    return render(request, template_name, contexto)

class MarcaView(SinPrivilegios, LoginRequiredMixin, ListView):
    permission_required = 'inv.view_marca'
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'
    login_url = 'bases_app:login'

class MarcaNew(SinPrivilegios, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    permission_required = 'inv.add_marca'
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv_app:marcas_list')
    login_url = 'bases_app:login'
    success_message = 'Nueva marca creada correctamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(SinPrivilegios, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'inv.change_marca'
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv_app:marcas_list')
    login_url = 'bases_app:login'
    success_message = 'Marca actualizada correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/inactivar.html'

    if not marca:
        return redirect('inv_app:marcas_list')

    if request.method == 'GET':
        contexto = {'obj': marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.error(request, 'Marca inactivada')
        return redirect('inv_app:marcas_list')

    return render(request, template_name, contexto)

class UniMedidaView(SinPrivilegios, LoginRequiredMixin, ListView):
    permission_required = 'inv.view_unimedida'
    model = UniMedida
    template_name = 'inv/unimedida_list.html'
    context_object_name = 'obj'
    login_url = 'bases_app:login'

class UniMedidaNew(SinPrivilegios, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    permission_required = 'inv.add_unimedida'
    model = UniMedida
    template_name = 'inv/unimedida_form.html'
    context_object_name = 'obj'
    form_class = UniMedidaForm
    success_url = reverse_lazy('inv_app:unimedidas_list')
    login_url = 'bases_app:login'
    success_message = 'Nueva unidad de medida creada correctamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class UniMedidaEdit(SinPrivilegios, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'inv.change_unimedida'
    model = UniMedida
    template_name = 'inv/unimedida_form.html'
    context_object_name = 'obj'
    form_class = UniMedidaForm
    success_url = reverse_lazy('inv_app:unimedidas_list')
    login_url = 'bases_app:login'
    success_message = 'Unidad de medida actualizada correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def unimedida_inactivar(request, id):
    unimedida = UniMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/inactivar.html'

    if not unimedida:
        return redirect('inv_app:unimedidas_list')

    if request.method == 'GET':
        contexto = {'obj': unimedida}

    if request.method == 'POST':
        unimedida.estado = False
        unimedida.save()
        messages.error(request, 'Unidad de medida inactivada')
        return redirect('inv_app:unimedidas_list')

    return render(request, template_name, contexto)

class ProductoView(SinPrivilegios, LoginRequiredMixin, ListView):
    permission_required = 'inv.view_producto'
    model = Producto
    template_name = 'inv/producto_list.html'
    context_object_name = 'obj'
    login_url = 'bases_app:login'

class ProductoNew(SinPrivilegios, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    permission_required = 'inv.add_producto'
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('inv_app:productos_list')
    login_url = 'bases_app:login'
    success_message = 'Nuevo producto creado correctamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoEdit(SinPrivilegios, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'inv.change_producto'
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('inv_app:productos_list')
    login_url = 'bases_app:login'
    success_message = 'Producto actualizado correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/inactivar.html'

    if not producto:
        return redirect('inv_app:productos_list')

    if request.method == 'GET':
        contexto = {'obj': producto}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        messages.error(request, 'Producto inactivado')
        return redirect('inv_app:productos_list')

    return render(request, template_name, contexto)