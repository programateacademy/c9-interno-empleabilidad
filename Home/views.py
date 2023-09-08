from django.shortcuts import render

    # Lógica de la vista aquí
def index(request):
    return render(request, 'index.html')

def home(request):
    return render (request, 'Home/home.html')
