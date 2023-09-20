from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from .company import Company
from .cohorteDate import cohorteDate

class Student (models.Model):
    name = models.CharField(max_length=50)
    cohorte = models.ForeignKey(cohorteDate, default=None, null=True, on_delete=models.SET_NULL )
    cedula = models.IntegerField(validators=[MaxValueValidator(999999999999)])
    password = models.CharField(max_length=128)
    company = models.ForeignKey(Company, null=True, on_delete= models.SET_NULL)
    employability = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.cohorte:
            current_cohorte = cohorteDate.objects.latest('cohorteNumber')
            self.cohorte = current_cohorte
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("student_detail",  args=[str(self.id)])
    