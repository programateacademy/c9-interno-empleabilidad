from django.contrib import admin

# Register your models here.

from .models.student import Estudiante
from .models.cohorteDate import Cohorte
from .models.company import Empresa

admin.site.register(Estudiante)
admin.site.register(Cohorte)
admin.site.register(Empresa)
