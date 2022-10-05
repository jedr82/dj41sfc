from email.policy import default
from django.db import models
from bases.models import ClaseModelo, ClaseModelo2
from cmp.models import Producto

class Cliente(ClaseModelo):
    NAT = 'Natural'
    JUR = 'Jurídica'
    TIPO_CLIENTE = [(NAT, 'Natural'),(JUR, 'Jurídica')]
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    celular = models.CharField(max_length=20, null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CLIENTE, default=NAT)

    def __str__(self):
        return '{} {}'.format(self.apellidos, self.nombres)

    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class FacturaEnc(ClaseModelo2):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.subtotal - self.descuento
        super(FacturaEnc, self).save()
    
    class Meta:
        verbose_name = 'Encabezado Factura'
        verbose_name_plural = 'Encabezados Factura'

class FacturaDet(ClaseModelo2):
    factura = models.ForeignKey(FacturaEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    
    def __str__(self):
        return '{}'.format(self.producto)
    
    def save(self):
        self.subtotal = float(float(int(self.cantidad))*float(self.precio))
        self.total = self.subtotal - float(self.descuento)
        super(FacturaDet, self).save()
        
    class Meta:
        verbose_name = 'Detalle Factura'
        verbose_name_plural = 'Detalles Facturas'