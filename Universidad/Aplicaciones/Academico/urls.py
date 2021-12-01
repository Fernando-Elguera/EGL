from django.urls import path 
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),    
    path('edicionCurso/<num>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<num>', views.eliminarCurso),
    path('salir/', views.salir, name="salir"),
    
    
]
