# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-09 00:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nivel3_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios',
            old_name='carrera',
            new_name='nombreCarrera',
        ),
    ]
