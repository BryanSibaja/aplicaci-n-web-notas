from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from notes.models import Nota

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditorForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ('titulo', 'cuerpo')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }
