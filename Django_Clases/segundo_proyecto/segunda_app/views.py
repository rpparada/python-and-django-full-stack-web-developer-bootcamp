# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>Mi Segunda Aplicacion</em>")

def helper(request):
    my_dirc = {'insertar_aqui':'Hola, esta es mi segunda aplicacion desde templates'}
    return render(request,'segunda_app/help.html',context=my_dirc)
