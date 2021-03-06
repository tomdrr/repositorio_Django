from django.urls import path #path me permite armar la config de URLS

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("" , views.inicio, name="Padre"),
    path("cursos/" , views.cursos , name="cursos"),
    #path("alta_curso/<nombre>" , views.alta_curso),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("contacto" , views.contacto , name="contacto"),
    path("profesores" , views.profesores , name="profesores"),
    path("entregables" , views.entregables , name="entregables"),
    path("alta_curso" , views.curso_formulario , name="Nuevo_curso"),
    path("buscar_curso" , views.buscar_curso),
    path("buscar" , views.buscar),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("editar_curso/" , views.editar , name="editar_curso"),
    path("login" , views.login_request , name="Login"),
    path("register" , views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="editarPerfil"),
    path("sobre_mi" , views.sobre_mi , name="sobre_mi")

    


]