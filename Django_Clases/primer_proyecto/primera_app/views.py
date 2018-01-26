# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me':'Hola, estoy desde primera_app/index.html'}
    return render(request,'primera_app/index.html',context=my_dict)
    # return HttpResponse("Hola Mundo!")
