from django.shortcuts import render

def dashboard_view(request):
    # Lógica de la vista aquí
    return render(request, 'dashboard.html')
