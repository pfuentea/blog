from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from time import gmtime,strftime,localtime

def index(request):
    respuesta="<h1>Hola Curso!</h1>"
    return HttpResponse(respuesta)

def dashboard(request):
    context={
            'title':'Dashboard'
        }
    return render(request, 'dashboard.html', context)

def login (request):
    context={
        'titulo':'Register',
        'nombre':'Pedro',
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
    elif request.method == 'GET':
        hora_actual = strftime("%Y-%m-%d %H:%M:%S %p", localtime())

    context={
        'hora':hora_actual,
        'title':'Time Display'
    }
    return render(request, 'time_display.html',context)
    