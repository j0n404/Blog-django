from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'titulo':'Inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'titulo':'Sobre nosotros'
    })

def register_page(request):
    register_form = RegisterForm()    

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Te has registrado correctamente')
            return redirect('inicio')
        
    
    return render(request, 'users/register.html',{
        'title':'Registro de usuarios',
        'register_form':register_form,
    })

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        contraseña = request.POST.get('contraseña')
        user = authenticate(request, username=username, password=contraseña)


        if user is not None:
            login(request, user)
            return redirect('inicio')



    return render(request, 'users/login.html', {
        'title':'Iniciar sesión'
    })

def logout_user(request):
    logout(request)
    return redirect('login')