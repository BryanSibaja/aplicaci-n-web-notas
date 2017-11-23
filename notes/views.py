from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request,'home.html')

def editor(request):
    return render(request, 'editor.html')

def registro(request):
    return render(request, 'registro.html')

def insertUser(request):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')