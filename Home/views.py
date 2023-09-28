from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import EstudianteLoginForm
from django.contrib import messages
from Dashboard.models.student import Estudiante
from django.contrib.auth.decorators import login_required

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
                
        return redirect('loginstudent')
    else:
        form = EstudianteLoginForm()
    return render(request, 'indexHome.html', {'form': form})



@login_required
def home(request):
    datos_usuario = Estudiante.objects.filter(username=request.user).first()
    if datos_usuario:
        return render(request, 'Home/home.html', {'datos_usuario': datos_usuario})


@login_required
def signout(request):
    logout(request)
    return redirect('index')


def index(request):
    return render (request, 'index.html')