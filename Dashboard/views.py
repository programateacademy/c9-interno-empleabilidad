from django.shortcuts import render

    # Lógica de la vista aquí
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render (request, 'Dashboard/dashboard.html')

def dashboardStudent(request):
    return render (request, 'Dashboard/dashboardStudent.html')
