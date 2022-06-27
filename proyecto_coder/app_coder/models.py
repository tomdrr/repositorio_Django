from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)  #model como va a ser el dataset en la base de datos sql
    camada = models.IntegerField()       #ya creada la app, voy a settings y "registro" la nueva app
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"

class Profesores(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Alumnos(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Camada: {self.camada}"

class Entregable(models.Model):
    
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha_entrega: {self.fecha_entrega} - Entregado: {self.entregado}"