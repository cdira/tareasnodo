from django.contrib import admin
from .models import Profesor, Asignatura, Escuela, RegistroProfesorEscuela
from django.contrib.auth.models import Group, User

# Register your models here.

admin.site.register(Asignatura)
admin.site.register(Escuela)
admin.site.unregister(Group)
admin.site.unregister(User)

class RegistroProfesorEscuelaInline(admin.TabularInline):
    model = RegistroProfesorEscuela
    extra = 1


class ProfesorAdmin(admin.ModelAdmin):
    inlines = [RegistroProfesorEscuelaInline,]
    list_display = ('nombre', 'apellido', 'email', 'fecha_contratacion')
    list_filter = ('fecha_contratacion', 'nombre',)
    list_per_page = 5


admin.site.register(Profesor, ProfesorAdmin)


