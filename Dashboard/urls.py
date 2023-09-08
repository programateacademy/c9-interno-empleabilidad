from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('admin', views.dashboard)
    # Otros patrones de URL aquí
]