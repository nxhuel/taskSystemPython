from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Curso

# Create your views here.


def home(request):
    listaCursos = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": listaCursos})


def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)

    return redirect('/')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos

    curso.save()
    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, 'El curso ha sido eliminado exitosamente.')
    return redirect('/')
