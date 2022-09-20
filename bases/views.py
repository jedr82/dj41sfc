from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, permission_required

from .models import Usuario
from .forms import UserForm

# Create your views here.
class HomePage(LoginRequiredMixin,generic.TemplateView):
    template_name = 'bases/index.html'
    login_url = 'bases_app:login'

class UserList(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    template_name = 'bases/users_list.html'
    login_url = 'bases_app:login'
    model = Usuario
    permission_required = 'bases_app:view_usuario'
    context_object_name = 'obj'


@login_required(login_url='bases_app:login')
@permission_required('bases.change_usuario', login_url='bases_app:login')
def user_admin(request, pk=None):
    template_name = 'bases/users_add.html'
    context = {}
    form = None
    obj = None

    if request.method == 'GET':
        if not pk:
            form = UserForm(instance = None)
        else:
            obj = Usuario.objects.filter(id=pk).first()
            form = UserForm(instance = obj)
        context['form'] = form
        context['obj'] = obj
    
    if request.method == 'POST':
        data = request.POST
        e = data.get('email')
        fn = data.get('first_name')
        ln = data.get('last_name')
        p = data.get('password')

        if pk:
            obj = Usuario.objects.filter(id=pk).first()
            if not obj:
                print('Error: usuario no existe')
            else:
                obj.email = e
                obj.first_name = fn
                obj.last_name = ln
                obj.password = make_password(p)
                obj.save()
        else:
            obj = Usuario.objects.create_user(email=e,password=p,first_name=fn,last_name=ln)
            print(obj.email,obj.password)
        return redirect('bases_app:users_list')

    return render(request, template_name, context)

class HomeSinPrivilegios(generic.TemplateView):
    template_name = 'bases/sin_privilegios.html'

class SinPrivilegios(PermissionRequiredMixin):
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url = 'bases_app:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))