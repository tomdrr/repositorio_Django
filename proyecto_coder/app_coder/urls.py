from django.urls import path #path me permite armar la config de URLS

from . import views

urlpatterns = [
    path("" , views.inicio),
    path("cursos/" , views.cursos , name="cursos"),
    path("alta_curso/<nombre>" , views.alta_curso),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("contacto" , views.contacto , name="contacto"),
    path("profesores" , views.profesores , name="profesores")


]