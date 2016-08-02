# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0002_remove_slide_enlace'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='enlace',
            field=models.CharField(default='http://www.tienda.com', max_length=256, verbose_name=b'Enlace'),
            preserve_default=False,
        ),
    ]
