from django.db import models
from django.utils import timezone
#from django.utils.http import urlquote >> ya fue deprecado y la siguiente linea le reemplaza
from urllib.parse import quote
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UsuarioManager

# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('direccion email'), max_length=254, unique=True)
    first_name = models.CharField(_('nombres'), max_length=30, blank=True)
    last_name = models.CharField(_('apellidos'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('es staff'), default=False, help_text=_('Indica si el usuario puede iniciar sesión en el admin'))
    is_active = models.BooleanField(_('activo'), default=True, help_text=_('Designa si este usuario debe ser tratado como activo' 'Deseleccione esto en lugar de eliminar cuentas.'))
    date_joined = models.DateTimeField(_('fecha registro'), default=timezone.now)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_absolute_url(self):
        return "/users/%s" % quote(self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True