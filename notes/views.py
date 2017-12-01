from django.shortcuts import render, redirect
from notes.forms import UserForm, EditorForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import login

def index(request):
    return render(request,'home.html')

def editor(request):
    if request.method == 'Post':
        form = EditorForm(request.Post)
        if form.is_valid():
            form.save()
        return redirect('home.html')
    else:
        form = EditorForm()
    return render(request, 'editor.html',{'form' : form})

def acceder(request):
    return login(request, template_name = "login.html", authentication_form= LoginForm)


def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,'home.html')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})
