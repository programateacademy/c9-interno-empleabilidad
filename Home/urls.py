from django.urls import path
from . import views

urlpatterns = [
    path('loginstudent/', views.loginstudent, name='loginstudent'),
    path('home/', views.home, name='home')
    # Otros patrones de URL aquí
]
