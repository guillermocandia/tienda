# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import solie.util.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.CharField(max_length=128, verbose_name=b'Mensaje', blank=True)),
                ('active', models.BooleanField(default=False, verbose_name=b'Activo')),
            ],
            options={
                'verbose_name': 'Aviso',
                'verbose_name_plural': 'Avisos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=solie.util.models.upload_image_to, verbose_name=b'Imagen')),
                ('titulo', models.CharField(max_length=256, verbose_name=b'Titulo', blank=True)),
                ('mensaje', models.TextField(verbose_name=b'Mensaje', blank=True)),
                ('active', models.BooleanField(default=False, verbose_name=b'Activo')),
                ('enlace', models.CharField(max_length=256, verbose_name=b'Enlace')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
            bases=(models.Model,),
        ),
    ]
