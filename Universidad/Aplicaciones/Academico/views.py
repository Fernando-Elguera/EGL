from django.db.models import fields
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from . models import Curso
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from time import gmtime, strftime
import pytz
from datetime import datetime
from .models import Curso
import csv

# Create your views here.

@login_required
def home(request):
    cursosListados = Curso.objects.all()

    return render(request, "gestionCursos.html", {"cursos": cursosListados})


def registrarCurso(request):
    
    edificio = request.POST['txtEdificio']
    fecharegistrada = datetime.now(pytz.timezone('US/Central'))
    fecharegistrada = fecharegistrada.strftime("%d-%m-%y %H:%M")
    numerodeparte = request.POST['txtNumerodeparte']
    descripcion = request.POST['txtDescripcion']
    modelo = request.POST['txtnumModelo']
    fecha = request.POST['txtFecha']
    solicitud = request.POST['txtSolicitud']
    fecha = strftime("%d-%m-%y", gmtime())
    
    curso = Curso.objects.create(
        edificio=edificio, fecharegistrada=fecharegistrada, numerodeparte=numerodeparte, descripcion=descripcion, modelo=modelo, fecha=fecha, solicitud=solicitud)

    messages.success(request, '¡Numero de parte registrado!')
    return redirect('/')


def edicionCurso(request, num):
    curso = Curso.objects.get(num=num)
    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request):
    num = request.POST['txtNum']
    edificio = request.POST['txtEdificio']
    numerodeparte = request.POST['txtNumerodeparte']
    descripcion = request.POST['txtDescripcion']
    modelo = request.POST['txtnumModelo']
    fecha = request.POST['txtFecha']
    solicitud = request.POST['txtSolicitud']
    curso = Curso.objects.get(num=num)

    curso.num = num
    curso.edificio = edificio
    curso.numerodeparte = numerodeparte
    curso.descripcion = descripcion
    curso.modelo = modelo
    curso.fecha = fecha
    curso.solicitud = solicitud
    curso.save()
    messages.success(request, '¡Numero de parte actualizado!')
    return redirect('/')


def eliminarCurso(request, num):    
    curso = Curso.objects.get(num=num)
    curso.delete()
    messages.success(request, '¡Numero de parte eliminado!')
    return redirect('/')


def salir(request):
    logout(request)
    return redirect('/')

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Materiales_EGL.csv"'

    writer = csv.writer(response)
    writer.writerow(['num','edificio', 'fecharegistrada', 'numerodeparte', 'descripcion', 'modelo', 'fecha', 'solicitud'])

    users = Curso.objects.all().values_list('num','edificio', 'fecharegistrada', 'numerodeparte', 'descripcion', 'modelo', 'fecha', 'solicitud')
    for user in users:
        writer.writerow(user)

    return response





    