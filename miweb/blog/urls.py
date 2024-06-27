from django.urls import path
from . import views

urlpatterns = [
    # ruta , donde la envio (el que hace el trabajo)
    path('', views.index , name='index'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('login/', views.login , name='login'),
    
]


