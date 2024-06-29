from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from time import gmtime,strftime,localtime
from .models import User

def index(request):
    respuesta="<h1>Hola Curso!</h1>"
    return HttpResponse(respuesta)

def dashboard(request):
    usuarios= User.objects.all() # select * from Users
    context={
            'title':'Dashboard',
            'usuarios':usuarios,
        }
    return render(request, 'dashboard.html', context)

def login (request):
    
    if request.method == 'POST':
        print(request.POST)
        email=request.POST['email']
        nombre=request.POST['name']
        password=request.POST['password']
        edad=request.POST['edad']
        # vamos a crear un User
        user=User.objects.create(name=nombre,email=email,password=password,edad=edad)

    if request.method == 'GET':
        nombre='Pedro'

    context={
        'titulo':'Register',
        'nombre':nombre,

    }
    return render(request, 'login.html',context)

def about(request):
    context={
        'title':'About'
    }
    return render(request, 'about.html',context)

def contacto(request):

    context={
        'title':'Contacto'
    }
    return render(request, 'contacto.html',context)

def galeria(request):
    context={
        'title':'Galeria'
    }
    return render(request, 'galeria.html',context)

# CREAR UNA RUTA time_display en la que llame a un método (VIEW) que nos diga la hora y la despliegue en el navegador, para eso usaremos la libreria time con sus métodos strftime() y gmtime()
# hora_actual = strftime("%Y-%m-%d %H:%M %p", gmtime())

def time_display(request):
    if request.method == 'POST':
        hora_actual ="HORA DE IRSE A CASA!"
    elif request.method == 'GET': # solicitud a traves de la URL o por un enlace
        hora_actual = strftime("%Y-%m-%d %H:%M:%S %p", localtime())

    context={
        'hora':hora_actual,
        'title':'Time Display'
    }
    return render(request, 'time_display.html',context)
    
def redireccion(request):

    return redirect('dashboard')

def editar_usuario(request,user_id):
    usuario = User.objects.get(id=user_id) #get sirve para buscar UN SOLO registro a travez del id
    
    if request.method == 'POST':
        usuario.email=request.POST['email']
        usuario.name=request.POST['name']
        usuario.password=request.POST['password']
        usuario.edad=request.POST['edad']
        usuario.save() # para que los cambios tengan efecto 

    context={
        'usuario':usuario,
    }
    
    return render(request, 'edit_user.html',context)

def borrar_usuario(request,user_id):
    usuario = User.objects.get(id=user_id)
    usuario.delete()
    return redirect('dashboard')