# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_www'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shortdescription',
            field=models.CharField(max_length=128, verbose_name=b'Unidad/Cantidad'),
            preserve_default=True,
        ),
    ]
