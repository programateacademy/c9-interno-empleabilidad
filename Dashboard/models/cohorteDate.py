from django.db import models
from django.urls import reverse

class Cohorte (models.Model):
    numerodecohorte = models.IntegerField()
    estadodelacorhorte = models.BooleanField(default=False)
    numerodeparticipantes = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.numerodecohorte)


    def get_absolute_url(self):
        return reverse("cohorte_detail", args=[str(self.id)])

    def add_participant (self):
        self.numberParticipants += 1 
        self.save()

    def remove_participant (self):
        if self.numberParticipants > 0:
            self.numberParticipants -= 1
            self.save()
    