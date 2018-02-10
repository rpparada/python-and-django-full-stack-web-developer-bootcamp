import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','nivel3_proyecto.settings')

import django
django.setup()

import random
from nivel3_app.models import Usuarios,Titulo
from faker import Faker

generaFake = Faker()
carreras = ['Abogado','Ingenieria Civil','Arquitectura']

def agrega_titulo():
    ti = Titulo.objects.get_or_create(nombreCarrera=random.choice(carreras),duracion=5)[0]
    ti.save()
    return ti

def popular(N=10):
    for entrada in range(N):

        tit = agrega_titulo()

        nombre_falso = generaFake.first_name()
        apellido_falso = generaFake.last_name()
        email_falso = generaFake.email()
        usuario = Usuarios.objects.get_or_create(nombre=nombre_falso,apellido=apellido_falso,email=email_falso,nombreCarrera=tit)[0]

if __name__ == '__main__':
    print('Cargando tabla(s)... ')
    popular(20)
    print('Rabla(s) cargada(s)!')
