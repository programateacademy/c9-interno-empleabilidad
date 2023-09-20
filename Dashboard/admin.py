from django.contrib import admin

# Register your models here.

from .models.student import Student
from .models.cohorteDate import cohorteDate
from .models.company import Company

class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'cohorte', 'dni', 'employability', 'company')
    search_fields = ('name', 'dni')
    ordering = ('-cohorte',)
    
class cohorteDateAdmin(admin.ModelAdmin):
    list_display = ('cohorteNumber', 'cohorteStatus', 'numberParticipants')
    search_fields = ('cohorteNumber',)
    ordering = ('-cohorteNumber',)
    
class CompanyAdmin(admin.ModelAdmin):
    ordering = ('companyName',)
    
admin.site.register(Student, StudentAdmin)
admin.site.register(cohorteDate, cohorteDateAdmin)
admin.site.register(Company, CompanyAdmin)
    
    
    
    
    
