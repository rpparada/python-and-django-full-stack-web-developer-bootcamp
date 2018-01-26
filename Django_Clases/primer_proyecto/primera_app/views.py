# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from primera_app.models import AccessRecord, Webpage, Topic

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # my_dict = {'insert_me':'Hola, estoy desde primera_app/index.html'}
    return render(request,'primera_app/index.html',context=date_dict)
    # return HttpResponse("Hola Mundo!")
