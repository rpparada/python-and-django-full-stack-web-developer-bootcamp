# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from formularioIngreso.models import Usuarios

# Create your views here.

def index(request):
    mi_diccionario = {'insertar_contenido':'Hola Mundo'}
    return render(request,'formularioIngreso/index.html',context=mi_diccionario)

def listaUsuario(request):
    lista_usuarios = Usuarios.objects.order_by('name')
    usuarios_dict = {'acceso_registros':lista_usuarios}
    return render(request,'formularioIngreso/listaUsuario.html', context=usuarios_dict)
