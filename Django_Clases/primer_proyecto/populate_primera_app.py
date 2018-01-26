import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','primer_proyecto.settings')

import django
django.setup()

import random
from primera_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()

topics = ['search','social','markplace','news','games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('Cargando tablas...')
    populate(20)
    print('Carga completa!')
