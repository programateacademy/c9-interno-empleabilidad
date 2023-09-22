from django.urls import path
from . import views

urlpatterns = [
    path('loginadmin/', views.loginadmin, name='loginAdmin'),
]

urlpatterns +=[
    path('cohortes/', views.cohortes, name='cohortes'),
    path('addcohorte/', views.addcohorte),
    path('students/', views.students),
    path('addstudent/', views.addstudent),
]
    # Otros patrones de URL aquí
