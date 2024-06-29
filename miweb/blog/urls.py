from django.urls import path
from . import views

urlpatterns = [
    # ruta , donde la envio (el que hace el trabajo)
    path('', views.index , name='index'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('login/', views.login , name='login'),
    # crear un menu en bootstrap con las secciones : 
    # Landing (index), Quienes somos(about), Contacto, Galeria
    #crear los templates (HTML)
    #crear las rutas (URLS.PY)
    #crear las vistas (VIEWS.PY)
    path('about/', views.about , name='about'),
    path('contacto/', views.contacto , name='contacto'),
    path('galeria/', views.galeria , name='galeria'),

    path('time_display/', views.time_display , name='time_display'),

    #ejemplo de redirección
    path('redireccion/', views.redireccion , name='redireccion'),
    #CRUD USER: EDITAR
    path('editar_usuario/<int:user_id>', views.editar_usuario , name='editar_usuario'),
    path('borrar_usuario/<int:user_id>', views.borrar_usuario , name='borrar_usuario'),

    
    
    



    
]


