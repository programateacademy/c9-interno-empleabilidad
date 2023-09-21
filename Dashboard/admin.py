from django.contrib import admin
#from django.utils.translation import gettext_lazy as _

# Register your models here.

from .models.student import Student
from .models.cohorteDate import cohorteDate
from .models.company import Company

# admin.site.index_title = _('Bienvenido')
# admin.site.site_header = _('Panel de administración de tu sitio')
# admin.site.site_title = _('Panel de administración')

# class MyAdminSite(admin.AdminSite):
#     def has_permission(self, request):
#         return request.user.is_active

#     def has_module_permission(self, request):
#         return False

# admin_site = MyAdminSite(name='myadmin')

class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'dni', 'employability', 'company')
    search_fields = ('name', 'dni')
    ordering = ('-cohorte',)
    
class cohorteDateAdmin(admin.ModelAdmin):
    list_display = ('cohorteNumber', 'cohorteStatus', 'numberParticipants')
    search_fields = ('cohorteNumber',)
    ordering = ('-cohorteNumber',)
    
class CompanyAdmin(admin.ModelAdmin):
    ordering = ('companyName',)
    
# class Studentviews(Student.Model):
#     list_display = ('name', 'employability', 'company')
    
admin.site.register(Student, StudentAdmin)
admin.site.register(cohorteDate, cohorteDateAdmin)
admin.site.register(Company, CompanyAdmin)


# admin.site.register(Student, Studentviews)

    
    
    
    
    
