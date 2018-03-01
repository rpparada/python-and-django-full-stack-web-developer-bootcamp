# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request,'index.html')

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CBV - Enviado")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['injectme'] = 'Insercion basica'
        return context

class ColegioLista(ListView):
    context_object_name = 'colegios'
    model = models.Colegio
    template_name = 'basic_app/colegio_lista.html'

class ColegioDetalle(DetailView):
    context_object_name = 'colegios_detalles'
    model = models.Colegio
    template_name = 'basic_app/colegio_detalle.html'
