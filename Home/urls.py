from django.urls import path
from . import views

urlpatterns = [
    path('loginstudent/', views.loginstudent),
    path('home/', views.home),
    
    # Otros patrones de URL aquí
]
