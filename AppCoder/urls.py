from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, cursos, inicio, profesores, estudiante, entregable


urlpatterns = [
    #path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    #path('estudiantes/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('', inicio, name="inicio"),
    path('cursos', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiante/', estudiante, name="estudiante"),
    path('entregable/', entregable, name="entregable"),
]