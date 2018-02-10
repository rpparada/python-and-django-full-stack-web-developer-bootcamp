# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.
class Titulo(models.Model):
    nombreCarrera = models.CharField(max_length=200)
    duracion = models.IntegerField()

    def __str__(self):
        return self.nombreCarrera + ', duracion ' + str(self.duracion)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    nombreCarrera = models.ForeignKey(Titulo)

    def __str__(self):
        return self.nombre + ', ' + self.apellido + ': ' + self.email

class UsuarioFormulario(ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

class TituloFormulario(ModelForm):
    class Meta:
        model = Titulo
        fields = '__all__'
