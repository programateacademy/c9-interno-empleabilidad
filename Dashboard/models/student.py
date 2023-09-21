from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from .company import Empresa
from .cohorteDate import Cohorte

class Estudiante (models.Model):
    nombre = models.CharField(max_length=50)
    cohorte = models.ForeignKey(Cohorte, default=None, null=True, on_delete=models.SET_NULL )
    dni = models.IntegerField(validators=[MaxValueValidator(999999999999)])
    contraseña = models.CharField(max_length=128)
    empresa = models.ForeignKey(Empresa, null=True, on_delete= models.SET_NULL)
    empleabilidad = models.BooleanField(default=False)




    def save(self, *args, **kwargs):
        if not self.cohorte:
            current_cohorte = Cohorte.objects.latest('')
            self.cohorte = current_cohorte
        self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("student_detail", args=[str(self.id)])