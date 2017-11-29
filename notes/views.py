from django.shortcuts import render, redirect
from notes.forms import UserForm, EditorForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,'home.html')
    else:
        form = UserCreationForm()
    return render(request, 'create_user.html', {'form': form})
