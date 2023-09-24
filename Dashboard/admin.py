from django.contrib import admin
#from django.utils.translation import gettext_lazy as _

# Register your models here.

from .models.student import Estudiante
from .models.cohorteDate import Cohorte
from.models.company import Empresa

# from .models.company import Empresa
# admin.site.index_title = _('Bienvenido')
# admin.site.site_header = _('Panel de administración de tu sitio')
# admin.site.site_title = _('Panel de administración')

# class MyAdminSite(admin.AdminSite):
#     def has_permission(self, request):
#         return request.user.is_active

#     def has_module_permission(self, request):
#         return False

# admin_site = MyAdminSite(name='myadmin')

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

