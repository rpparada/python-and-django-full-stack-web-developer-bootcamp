# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-09 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nivel3_app', '0003_auto_20180209_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo',
            name='nombreCarrera',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
