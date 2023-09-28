from django.urls import path
from . import views

urlpatterns = [
    path('loginstudent/', views.loginstudent, name='loginstudent'),
    path('home/', views.home, name='home'),
    path('', views.index, name='index')
    # Otros patrones de URL aquí
]
