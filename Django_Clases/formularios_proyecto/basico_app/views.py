# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . import forms
# Create your views here.

def index(request):
    return render(request,'basico_app/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Validacion exitosa')
            print('Nombre : '+form.cleaned_data['name'])
            print('Email : '+form.cleaned_data['email'])
            print('Texto : '+form.cleaned_data['text'])
    return render(request,'basico_app/formulario.html',{'form':form})
