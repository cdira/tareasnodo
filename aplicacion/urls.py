from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("formulario", views.formulario, name="formulario"),
    path('create/', views.create, name='create'),
    path('register/', views.register, name="register"),
    path('crearusuario/', views.crear_usuario, name="crearusuario"),
    path('consultaprofesores/', views.consulta_profesores, name='consultaprofesores'),
    path('crearescuela/', views.crearescuela, name='crearescuela'),
    path('listarescuela/', views.listarescuela, name='listarescuela'),
    path('editarescuela/<int:id>', views.editarescuela, name='editarescuela'),
    path('eliminarescuela/<int:id>', views.eliminarescuela, name='eliminarescuela'),
    path('crearasignatura/<int:id>', views.crearasignatura, name='crearasignatura'),
    path('listarasignatura/<int:id>', views.listarasignatura, name='listarasignatura'),
]
