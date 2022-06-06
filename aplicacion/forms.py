from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profesor, Escuela, Asignatura

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields =('nombre', 'apellido', 'edad', 'email', 'fecha_contratacion', 'escuela')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmacion contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class LoginForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

class EscuelaForm(forms.ModelForm):
    class Meta:
        model = Escuela
        fields = ['nombre', 'direccion', 'email']

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'profesor', 'escuela']

#class ProfesorForm(forms.Form):
 #   nombre = forms.CharField(max_length=50, required=True)
  #  apellido = forms.CharField(max_length=50, required=True)
  #  edad =forms.IntegerField(required=True)
  #  email = forms.EmailField(required=True)
  #  fecha_contratacion = forms.DateField(required=True)
