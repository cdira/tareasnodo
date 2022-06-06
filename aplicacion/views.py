
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .backend import MyBackend

from aplicacion.backend import MyBackend

from .models import Profesor, Escuela, Asignatura

from .forms import ProfesorForm, AsignaturaForm, UserRegistrationForm, LoginForm, EscuelaForm


myBackend=MyBackend()
# Create your views here.
#@login_required
def index(request):

    listado = Profesor.objects.all()
    edades = Profesor.objects.get(edad=32).nombre

    data = {
        'context':listado,
        'cantidad':len(listado),
        'edades': edades,
    }

    return render(request, 'aplicacion/index.html', {'context':data['context']})

def formulario(request):
    return render(request, 'aplicacion/formulario.html')

def create(request):
    form = ProfesorForm()
    if request.method == 'POST':
        #print(request.POST)
        form = ProfesorForm(request.POST)

        if form.is_valid():
            #print('Valido')
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.edad = form.cleaned_data['edad']
            profesor.email = form.cleaned_data['email']
            profesor.fecha_contratacion = form.cleaned_data['fecha_contratacion']
            #profesor.escuela = form.cleaned_data['escuela']
            profesor.save()

        else:
            print('Invalido')
        return redirect('/aplicacion')

    return render(request, 'aplicacion/create.html', {'form':form})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form':form}

    return render(request, 'aplicacion/register.html', context)

def login(request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        usuario=form.cleaned_data['nombre']
        clave=form.cleaned_data['password']
        user= MyBackend.authenticate(request, username=usuario, password=clave)
        if user is not None:
            auth_login(request, user)
        return render(request, 'aplicacion/index.html', {'user':user})
    else:
        form = LoginForm()
        return render(request, 'aplicacion/login.html', {'form':form})

def crear_usuario(request):
    user = User(username='daniela')
    user.set_password("password")
    user.save()
    return HttpResponse(f'Usuario creado exitosamente')

def consulta_profesores(request):

    #context = Profesor.objects.all()

    #context = Profesor.objects.raw('select * from aplicacion_profesores')
    for prof in Profesor.objects.raw('select * from aplicacion_profesores'):
        print(prof)

    return render(request, 'aplicacion/consulta_profesores.html', {'context':prof})

def crearescuela(request):
    form = EscuelaForm()
    if request.method == "POST":
        form = EscuelaForm(data=request.POST)
        escuela = form.save(commit=False)
        escuela.save()
        return redirect('/listarescuela')
        #return HttpResponse(f"La escuela {escuela.nombre} fue creada exitosamente.")
    else:
        return render(request, 'aplicacion/crearescuela.html', {'form':form})

def listarescuela(request):
    escuela = Escuela.objects.all()
    return render(request, 'aplicacion/listarescuela.html', {'escuela':escuela})

def editarescuela(request, id):
    escuela = Escuela.objects.get(pk=id)
    form = EscuelaForm(instance=escuela)
    if request.method == "POST":
        form = EscuelaForm(data=request.POST, instance=escuela)
        form.save()
        return redirect('listarescuela')
    else:
        return render(request, 'aplicacion/editarescuela.html', {'form':form})    

def eliminarescuela(request):
    escuela = Escuela.objects.get(pk=id)
    escuela.delete()
    return redirect('listarescuela')

def crearasignatura(request):
    form = AsignaturaForm()
    if request.method == "POST":
        form = AsignaturaForm(data=request.POST)
        asignatura = form.save(commit=False)
        asignatura.save()
        return redirect('/listarasignatura')
     
    else:
        return render(request, 'aplicacion/crearasignatura.html', {'form':form})

def listarasignatura(request):
    asignatura = Asignatura.objects.all()
    return render(request, 'aplicacion/listarasignatura.html', {'asignatura':asignatura})


