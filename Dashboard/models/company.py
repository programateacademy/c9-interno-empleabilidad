from django.db import models
from django.urls import reverse

class Empresa (models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("company_detail", args=[str(self.id)])
    

    