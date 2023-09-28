from django.shortcuts import render, redirect
# from .forms import EstudianteLoginForm
# from Dashboard.models.student import Estudiante
from django.contrib.auth import authenticate, login

# def loginstudent(request):

#     return render(request, 'indexHome.html')

# def loginstudent(request):
#     authentication_form = EstudianteLoginForm
#     return render(request, 'Home/indexHome.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import EstudianteLoginForm

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import EstudianteLoginForm

# def loginstudent(request):
#     if request.method == 'POST':
#         form = EstudianteLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username_or_dni')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('Home/home.html')
#     else:
#         form = EstudianteLoginForm()
#     return render(request, 'indexHome.html', {'form': form})
from django.contrib import messages

def loginstudent(request):
    if request.method == 'POST':
        form = EstudianteLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username_or_dni')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Los detalles de inicio de sesión no son válidos')
    else:
        form = EstudianteLoginForm()
    return render(request, 'indexHome.html', {'form': form})



def home(request):
    return render (request, 'Home/home.html')

def index(request):
    return render (request, 'index.html')
