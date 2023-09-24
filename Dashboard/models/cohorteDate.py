from django.db import models
from django.urls import reverse


class Cohorte(models.Model):
    OPCIONES_ESTADO = (
        ('Activa', 'Activa'),
        ('No Activa', 'No Activa')
    )

    numerodecohorte = models.IntegerField()
    estadodelacorhorte = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Activa')
    numerodeestudiantes = models.PositiveIntegerField(editable=False, default=0)


    def actualizar_numerodeestudiantes(self):
        self.numerodeestudiantes = self.estudiante_set.count()
        self.save()


    def __str__(self):
        return str(self.numerodecohorte)

    def obtener_palabra(self):
        if self.estadodelacorhorte == 'Activa':
            return "Activa"
        elif self.estadodelacorhorte == 'No Activa':
            return "No Activa"
        else:
            return "Ninguna opción seleccionada"

    def get_absolute_url(self):
        return reverse("cohorte_detail", args=[str(self.id)])
