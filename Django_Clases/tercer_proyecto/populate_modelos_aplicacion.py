import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tercer_proyecto.settings')

import django
django.setup()

import random
from modelos_aplicacion.models import Usuarios
from faker import Faker

generaFake = Faker()

def popular(N=10):
    for entrada in range(N):
        nombre_falso = generaFake.first_name()
        apellido_falso = generaFake.last_name()
        email_falso = generaFake.email()
        # email_falso = generaFake.email(*args, **kwargs)

        usuario = Usuarios.objects.get_or_create(nombre=nombre_falso,apellido=apellido_falso,email=email_falso)[0]

if __name__ == '__main__':
    print('Cargando tabla(s)... ')
    popular(20)
    print('Rabla(s) cargada(s)!')
