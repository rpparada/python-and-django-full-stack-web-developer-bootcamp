# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)

    def __str__(self):
        return nombre + ', ' + apellido + ': ' + email
