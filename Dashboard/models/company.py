from django.db import models
from django.urls import reverse

class Company (models.Model):
    companyName = models.CharField(max_length=50)

    def __str__(self):
        return self.companyName

    def get_absolute_url(self):
        return reverse("company_detail", args=[str(self.id)])
    

    