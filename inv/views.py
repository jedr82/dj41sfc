from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView

from inv.forms import CategoriaForm, SubCategoriaForm, MarcaForm
from inv.models import Categoria, SubCategoria, Marca


class CategoriaView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases_app:login'

class CategoriaNew(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv_app:categorias_list')
    login_url = 'bases_app:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv_app:categorias_list')
    login_url = 'bases_app:login'

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
        return redirect('inv_app:categorias_list')

    return render(request, template_name, contexto)

class SubCategoriaView(LoginRequiredMixin, ListView):
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases_app:login'

class SubCategoriaNew(LoginRequiredMixin, CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv_app:subcategorias_list')
    login_url = 'bases_app:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, UpdateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv_app:subcategorias_list')
    login_url = 'bases_app:login'

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
        return redirect('inv_app:subcategorias_list')

    return render(request, template_name, contexto)

class MarcaView(LoginRequiredMixin, ListView):
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'
    login_url = 'bases_app:login'

class MarcaNew(LoginRequiredMixin, CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv_app:marcas_list')
    login_url = 'bases_app:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv_app:marcas_list')
    login_url = 'bases_app:login'

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
        return redirect('inv_app:marcas_list')

    return render(request, template_name, contexto)