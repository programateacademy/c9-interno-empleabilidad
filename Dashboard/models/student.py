from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from .company import Empresa
from .cohorteDate import Cohorte
from django.contrib.auth.models import User
from django.db import IntegrityError

class Estudiante(models.Model):
    OPCIONES = (
        ('Empleado', 'Empleado',),
        ('En proceso de empleabilidad', ('En proceso de empleabilidad')),
        ('Desempleado', ('Desempleado'))
    )
    username = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    cohorte = models.ForeignKey(Cohorte, default=None, null=True, on_delete=models.SET_NULL)
    dni = models.IntegerField(validators=[MaxValueValidator(999999999999)], unique=True)
    empresa = models.ForeignKey(Empresa, null=True, on_delete= models.SET_NULL)
    contraseña = models.CharField(max_length=128)
    empleabilidad = models.CharField(max_length=30, choices=OPCIONES, default='Empleado')



    def save(self, *args, **kwargs):
        if self.pk is None:
            try:
                user = User.objects.create_user(
                    username=self.username,
                    password=self.contraseña,
                    first_name=self.nombre,
                    last_name=self.apellido,
            )
                self.user = user
            except IntegrityError:
                raise ValueError("Un usuario con ese nombre de usuario ya existe")
        super().save(*args, **kwargs)
        if self.cohorte:
            self.cohorte.actualizar_numerodeestudiantes()

    def __str__(self):
        return self.nombre


def obtener_palabra(self):
            if self.seleccion == 'Empleado':
                return "Empleado"
            elif self.seleccion == 'En proceso de empleabilidad':
                return "En proceso de empleabilidad"
            elif self.seleccion == 'Desempleado':
                return "Desempleado"
            else:
                return "Ninguna opción seleccionada"

def get_absolute_url(self):
            return reverse("student_detail", args=[str(self.id)])