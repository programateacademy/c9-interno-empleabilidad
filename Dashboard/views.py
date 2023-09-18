from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
from django.contrib.auth import login



    # Lógica de la vista aquí
    
def loginadmin(request):#login para que admin ingrese
    return render (request, 'index.html')






def addcohorte(request):  #para agregar cohortes
    return render(request, 'Dashboard/dashboardAddCohorte.html')

def cohortes(request):  #para agregar cohortes
    return render(request, 'Dashboard/dashboardCohorte.html')


def addstudent(request): 
    return render(request, 'Dashboard/dashboardAddStudent.html')

def students(request): 
    return render(request, 'Dashboard/dashboardStudent.html')



# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html', {
#             'form': UserCreationForm
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(
#                     username=request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('signup')
#             except IntegrityError :
#                 return render(request, 'signup.html', {
#                     'form': UserCreationForm,
#                     "error": 'User alredy exits'
#                 })
#         return render(request, 'signup.html', {
#             'form': UserCreationForm,
#             "error": 'Password do not match'
#         })

