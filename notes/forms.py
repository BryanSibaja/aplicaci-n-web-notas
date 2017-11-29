from django import forms
from django.contrib.auth.models import User
from notes.models import Nota

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name')
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditorForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ('titulo', 'cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }
