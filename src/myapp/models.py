from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion_minutos = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class Turno(models.Model):

    METODO_PAGO = [
        ('EFECTIVO', 'Efectivo'),
        ('TRANSFERENCIA', 'Transferencia'),
    ]

    ESTADO_TURNO = [
        ('PENDIENTE', 'Pendiente'),
        ('ATENDIDO', 'Atendido'),
        ('AUSENTE', 'Ausente'),
        ('CANCELADO', 'Cancelado'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    fecha = models.DateField()
    hora = models.TimeField()

    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO)
    estado = models.CharField(max_length=20, choices=ESTADO_TURNO, default='PENDIENTE')

    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('fecha', 'hora')
        ordering = ['fecha', 'hora']

    def clean(self):
        if self.fecha.weekday() in [0, 6]:
            raise ValidationError("No se trabajan turnos los lunes ni domingos.")

    def __str__(self):
        return f"{self.cliente.username} - {self.fecha} {self.hora}"