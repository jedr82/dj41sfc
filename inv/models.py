from django.db import models
from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField('Descripción', max_length=100, help_text='Descripión de la categoría', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField('Descripción', max_length=100, help_text='Descripción de la subcategoria')

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name = 'Sub Categoría'
        verbose_name_plural = 'Sub Categorías'
        unique_together = ('categoria','descripcion')