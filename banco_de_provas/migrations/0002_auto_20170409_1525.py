# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-09 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco_de_provas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prova',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]
