from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    respuesta="<h1>Hola Curso!</h1>"
    return HttpResponse(respuesta)

def dashboard(request):

    return render(request, 'dashboard.html')

def login (request):

    context={
        'titulo':'Register',
        'nombre':'Pedro',
    }
    
    return render(request, 'login.html',context)