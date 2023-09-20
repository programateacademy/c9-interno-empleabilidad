from django.urls import path
from . import views

urlpatterns = [
    path('loginadmin/', views.loginadmin),
    path('cohortes/', views.cohortes),
    path('addcohorte/', views.addcohorte),
    path('students/', views.students),
    path('addstudent/', views.addstudent),
    # path('signup/', views.signup),

    # Otros patrones de URL aquí
]
