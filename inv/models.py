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

class Marca(ClaseModelo):
    descripcion = models.CharField('Marca', max_length=100, help_text='Descripción de la marca', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class UniMedida(ClaseModelo):
    descripcion = models.CharField('Marca', max_length=100, help_text='Descripción de la unidad de medida', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UniMedida, self).save()

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'

class Producto(ClaseModelo):
    codigo = models.CharField('Codigo', max_length=20, unique=True)
    codigo_barra = models.CharField('Codigo de Barras', max_length=15)
    descripcion = models.CharField('Descripción', max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UniMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        unique_together = ('codigo','codigo_barra')