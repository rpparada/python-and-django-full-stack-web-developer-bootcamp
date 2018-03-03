# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Colegio(models.Model):
    name = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    ubicacion = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:details',kwargs={'pk':self.pk})

class Alumno(models.Model):
    name = models.CharField(max_length=256)
    edad = models.PositiveIntegerField()
    colegio = models.ForeignKey(Colegio,related_name='alumnos')

    def __str__(self):
        return self.name

# usuario: rodrigo
# contra: ladesiempre
