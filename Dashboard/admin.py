from django.contrib import admin

# Register your models here.

from .models.student import Estudiante
from .models.cohorteDate import Cohorte
from.models.company import Empresa

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'dni', 'empleabilidad', 'empresa')
    search_fields = ('nombre', 'dni')
    ordering = ('-cohorte',)
    
class CohorteAdmin(admin.ModelAdmin):
    list_display = ('numerodecohorte', 'estadodelacorhorte', 'numerodeparticipantes')
    search_fields = ('numerodecohorte',)
    ordering = ('-numerodecohorte',)
    
class EmpresaAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    
    
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Cohorte , CohorteAdmin)
admin.site.register(Empresa, EmpresaAdmin)

