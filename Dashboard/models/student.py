from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from .company import Empresa
from .cohorteDate import Cohorte
from django.db.models.signals import post_save
from django.dispatch import receiver

class Estudiante (models.Model):
    OPCIONES = (
        ('Empleado', 'Empleado',),
        ('En Proceso', ('En Proceso')),
        ('Desenpleado', ('Desempleado'))
    )
    nombre = models.CharField(max_length=50)
    cohorte = models.ForeignKey(Cohorte, default=None, null=True, on_delete=models.SET_NULL)
    dni = models.IntegerField(validators=[MaxValueValidator(999999999999)])
    contraseña = models.CharField(max_length=128)
    empresa = models.ForeignKey(Empresa, null=True, on_delete= models.SET_NULL)
    empleabilidad = models.CharField(max_length=15, choices=OPCIONES, default='Empleado')



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cohorte:
            self.cohorte.actualizar_numerodeestudiantes()


    def __str__(self):
        return self.nombre


def obtener_palabra(self):
            if self.seleccion == 'Empleado':
                return "Empleado"
            elif self.seleccion == 'En Proceso':
                return "En Proceso"
            elif self.seleccion == 'Desenpleado':
                return "Desenpleado"
            else:
                return "Ninguna opción seleccionada"

def get_absolute_url(self):
            return reverse("student_detail", args=[str(self.id)])