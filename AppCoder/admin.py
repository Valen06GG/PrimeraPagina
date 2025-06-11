from django.contrib import admin

from .models import Estudiante, Profesores, Curso, Entregable

admin.site.register(Estudiante)
admin.site.register(Profesores)
admin.site.register(Curso)
admin.site.register(Entregable)
