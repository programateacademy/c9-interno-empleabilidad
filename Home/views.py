from django.shortcuts import render

    # Lógica de la vista aquí
def loginstudent(request):
    return render(request, 'indexHome.html')

def home(request):
    return render (request, 'Home/home.html')

