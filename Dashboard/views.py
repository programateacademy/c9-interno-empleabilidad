from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.contrib.auth import login




    # Lógica de la vista aquí
    
    #login para que admin ingrese
def loginadmin(request):
    if request.method == 'GET':
        return render(request, 'index.html', {"form": AuthenticationForm})
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is None:
            return render(request, 'index.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('cohortes')

def cohortes(request):  # para agregar cohortes

    return render(request, 'Dashboard/dashboardCohorte.html')



def cohortes(request):  #para agregar cohortes
    return render(request, 'Dashboard/dashboardCohorte.html')





def addcohorte(request):  #para agregar cohortes
    return render(request, 'Dashboard/dashboardAddCohorte.html')



def addstudent(request): 
    return render(request, 'Dashboard/dashboardAddStudent.html')

def students(request): 
    return render(request, 'Dashboard/dashboardStudent.html')



from django.contrib.auth import authenticate, login

def user_login(request):
    '''
    Login
    '''
    if request.method == 'POST':
            user = authenticate(
                username=request.POST['email'],
                password=request.POST['password']
            )
            if user is not None:
                login(request, user)
                return redirect(cohortes)



