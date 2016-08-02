# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_product_www'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='www',
            field=models.BooleanField(default=False, verbose_name=b'Mostrar en Portada'),
            preserve_default=True,
        ),
    ]
