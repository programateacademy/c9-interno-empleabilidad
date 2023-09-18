from django.contrib import admin

# Register your models here.

from .models.student import Student
from .models.cohorteDate import cohorteDate
from .models.company import Company

admin.site.register(Student)
admin.site.register(cohorteDate)
admin.site.register(Company)