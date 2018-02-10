# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from nivel3_app.models import Titulo,Usuarios
from nivel3_app.forms import UsusarioFormulario
# from django.http import HttpResponse

# Create your views here.

def index(request):
    mi_dict = {'insertar_aqui':'Hola Mundo3'}
    return render(request,'nivel3_app/index.html',context=mi_dict)
    # return HttpResponse('Hola Mundo')

def usuarios(request):
    lista_usuarios = Usuarios.objects.order_by('nombre')
    direct_usuarios = {'usuarios':lista_usuarios}
    return render(request,'nivel3_app/usuarios.html',context=direct_usuarios)

def titulos(request):
    lista_titulos = Titulo.objects.order_by('nombreCarrera')
    direct_titutlos = {'titulos':lista_titulos}
    return render(request,'nivel3_app/titulos.html',context=direct_titutlos)

def form_nuevo_usuario(request):
    form = UsusarioFormulario()

    if request.method == 'POST':
        form = UsusarioFormulario(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Validacion Exitosa')
            print('Nombre :'+form.cleaned_data['nombre'])
            print('Apellido :'+form.cleaned_data['apellido'])
            print('Email :'+form.cleaned_data['email'])
            return index(request)
        else:
            print('Error en formulario')

    return render(request,'nivel3_app/formulario.html',{'form':form})
