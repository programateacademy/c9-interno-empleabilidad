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

    def __str__(self):
        return str(self.numerodecohorte)

    def agregar_estudiante(self, estudiante):
        if estudiante.cohorte != self:
            estudiante.cohorte = self
            estudiante.save()
            self.actualizar_numerodeestudiantes()

    def eliminar_estudiante(self, estudiante):
        if estudiante.cohorte == self:
            estudiante.cohorte = None
            estudiante.save()
            self.actualizar_numerodeestudiantes()

    def actualizar_numerodeestudiantes(self):
        self.numerodeestudiantes = self.estudiantes.count()
        self.save()

    def obtener_palabra(self):
        if self.estadodelacorhorte == 'Activa':
            return "Activa"
        elif self.estadodelacorhorte == 'No Activa':
            return "No Activa"
        else:
            return "Ninguna opción seleccionada"

    def get_absolute_url(self):
        return reverse("cohorte_detail", args=[str(self.id)])
