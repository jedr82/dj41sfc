from django.db import models

#Para los signals
from django.db.models import Sum
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver

from bases.models import ClaseModelo
from inv.models import Producto


class Proveedor(ClaseModelo):
    descripcion = models.CharField('Nombre de proveedor', max_length=100, unique=True)
    direccion = models.CharField('Direccion', max_length=250, null=True, blank=True)
    contacto = models.CharField('Contacto', max_length=100)
    telefono = models.CharField('Telefono', max_length=15, null=True, blank=True)
    email = models.CharField('Email', max_length=150, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']

class ComprasEnc(ClaseModelo):
    fecha_compra = models.DateField('Fecha de Compra', null=True, blank=True)
    observacion = models.TextField('Observacion', blank=True, null=True)
    nro_factura = models.CharField('NroFactura', max_length=15)
    fecha_factura = models.DateField('Fecha de factura')
    subtotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        self.total = self.subtotal-self.descuento
        super(ComprasEnc, self).save()

    class Meta:
        verbose_name = 'Encabezado de Compra'
        verbose_name_plural = 'Encabezados de compras'

class ComprasDet(ClaseModelo):
    compra = models.ForeignKey(ComprasEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    precio_prv = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    costo = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.subtotal = float(float(int(self.cantidad)) * float(self.precio_prv))
        self.total = self.subtotal - float(self.descuento)
        super(ComprasDet, self).save()

    class Meta:
        verbose_name = 'Detalle Compra'
        verbose_name_plural = 'Detalles de Compras'


@receiver(post_delete, sender=ComprasDet)
def detalle_compra_borrar(sender, instance, **kwargs):
    id_producto = instance.producto.id
    id_compra = instance.compra.id

    enc = ComprasEnc.objects.filter(pk=id_compra).first()

    if enc:
        sub_total = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('subtotal'))
        descuento = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('descuento'))
        enc.subtotal = sub_total['subtotal__sum']
        enc.descuento = descuento['descuento__sum']
        enc.save()

    prod = Producto.objects.filter(pk=id_producto).first()

    if prod:
        cantidad = int(prod.existencia)-int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()


@receiver(post_save, sender=ComprasDet)
def detalle_compra_guardar(sender, instance, **kwargs):
    id_producto = instance.producto.id
    fecha_compra = instance.compra.fecha_compra

    prod = Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        prod.ultima_compra = fecha_compra
        prod.save()