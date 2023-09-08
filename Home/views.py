from django.shortcuts import render

def home_view(request):
    # Lógica de la vista aquí
    return render(request, 'home.html')
