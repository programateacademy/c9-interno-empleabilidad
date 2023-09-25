from django.urls import path
from . import views

urlpatterns = [
    path('loginstudent/', views.loginstudent),
    path('home/', views.home),
    path('cambio_contraseña/', views.cambio_contraseña)
    # Otros patrones de URL aquí
]
