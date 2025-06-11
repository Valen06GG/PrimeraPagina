from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, cursos, inicio, profesores, estudiante, entregable

from AppCoder import views

urlpatterns = [
    #path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    #path('estudiantes/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('', views.inicio, name="inicio"),
    path('cursos', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiante/', views.estudiante, name="estudiante"),
    path('entregable/', views.entregable, name="entregable"),
]