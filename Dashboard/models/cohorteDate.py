from django.db import models
from django.urls import reverse

class Cohorte (models.Model):
    OPCIONES = (
        ('Activa', 'Activa'),
        ('No Activa', ('No Activa'))
    )
    numerodecohorte = models.IntegerField()
    estadodelacorhorte = models.CharField(max_length=15, choices=OPCIONES, default='Activa')
    numerodeparticipantes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.numerodecohorte)

    def obtener_palabra(self):
        if self.seleccion == 'Activa':
            return "Activa"
        elif self.seleccion == 'No Activa':
            return "No Activa"
        else:
            return "Ninguna opción seleccionada"

    def get_absolute_url(self):
        return reverse("cohorte_detail", args=[str(self.id)])

    def add_participant (self):
        self.numberParticipants += 1 
        self.save()

    def remove_participant (self):
        if self.numberParticipants > 0:
            self.numberParticipants -= 1
            self.save()
    