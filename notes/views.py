"""Modulo controlador de la aplicacion de notas"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, views
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from notes.forms import UserForm, EditorForm, LoginForm
from notes.models import Nota, Libro

def index(request):
    """Carga la pagina de inicio"""
    return render(request,'home.html')

def editor(request):
    """Carga la iterfaz del editor de notas"""
    if request.method == 'POST':
        form = EditorForm(request.POST)
        n = Nota(titulo="provando", 
        cuerpo="lo que sea", 
        libro=Libro.objects.get(id=2))
        n.save()
    else:
        form = EditorForm()
    return render(request, 'editor.html', {'form' : form})

def acceder(request):
    """Inicio de sesion"""
    return views.login(request, template_name="login.html", authentication_form=LoginForm)

@csrf_exempt
def borrarNota(request):
    idNota = request.POST.get('id')
    nota = Nota.objects.get(id=idNota)
    libro = nota.libro_id
    nota.delete()
    notas = Nota.objects.filter(libro_id=libro)
    respuesta = serialize('json',notas)
    return HttpResponse(respuesta, content_type="application/json")

@csrf_exempt
def nuevoCuaderno(request):
    n = request.POST.get('cua')
    libro = Libro(nombre=n, pertenece= User.objects.get(id=request.user.id) )
    libro.save()
    libros = Libro.objects.filter(pertenece_id=request.user.id)
    respuesta = serialize('json', libros)
    return HttpResponse(respuesta, content_type="application/json")

def listarLibros(request):
    libros = Libro.objects.filter(pertenece_id=request.user.id)
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            form.save()
            form = EditorForm()
    else:
        form = EditorForm()

    contexto = {'libros':libros, 'form':form}
    return render(request, 'libros.html', contexto)

@csrf_exempt
def listarNotas(request):
    if request.method == 'POST':
        libro_id = request.POST.get('libro')
        notas = Nota.objects.filter(libro=libro_id)
        respuesta = serialize('json', notas)
        return HttpResponse(respuesta, content_type="application/json")


def registro(request):
    """Crea un nuevo usuario"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            redirect('/editor/')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})
