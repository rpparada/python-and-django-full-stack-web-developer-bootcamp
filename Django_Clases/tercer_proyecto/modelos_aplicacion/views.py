# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from modelos_aplicacion.models import Usuarios

# Create your views here.
def index(request):
    lista_usuarios = Usuarios.objects.order_by('nombre')
    usuarios_dicc = {'acceso_reg':lista_usuarios}
    return render(request,'modelos_aplicacion/index.html',context=usuarios_dicc)
