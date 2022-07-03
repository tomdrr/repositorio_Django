from this import d
from django.http import HttpResponse
from django.shortcuts import render

from app_coder.models import *   #importo desde app_coder.models la clase Curso
from app_coder.forms import Curso_formulario
from django.template import loader
# Create your views here.


def inicio(request):
    return render(request , "plantillas.html")


def cursos(request):
    cursos = Curso.objects.all() #importo toda la data de los cursos
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


"""
def alta_curso(request, nombre):
    curso= Curso (nombre=nombre , camada = 12365)
    curso.save()
    texto =f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)
"""

def alumnos(request):
    return render(request , "alumnos.html")


def contacto(request):
    return render(request , "contacto.html")

def profesores(request):
    return render(request , "profesores.html")

def entregables(request):
    return render(request , "entregables.html")





def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data

            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'] )
            curso.save()
            return render(request , "formulario.html")
        
    return render(request, "formulario.html")



def buscar_curso(request):
    return render(request , "buscar_curso.html")


def buscar (request):
    if request.POST ['nombre']:
        nombre = request.POST['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request , "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("No se encontro el curso")
  



def elimina_curso(request , id):

    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()
    return render(request , "cursos.html" , {"cursos": curso})



def editar( request , id):

    curso = Curso.objects.get(id=id)
    
    if request.method == "POST":

        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso = Curso.objects.all()
            return render(request , "cursos.html" , {"cursos": curso})

    else:
        mi_formulario = Curso_formulario(initial={'nombre':curso.nombre , 'camada':curso.camada})

    return render(request , "editar_curso.html" , {"mi_formulario":mi_formulario , "curso": curso})