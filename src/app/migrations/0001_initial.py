# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models
from django.conf import settings
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name=b'Creado')),
                ('modified', models.DateTimeField(verbose_name=b'Modificado')),
                ('checked_out', models.BooleanField(default=False, verbose_name=b'Confirmado')),
                ('user', models.ForeignKey(verbose_name=b'Usuario', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name=b'Nombre')),
                ('slug', models.SlugField(max_length=64, verbose_name=b'Slug')),
                ('order', models.IntegerField(default=0, verbose_name=b'Orden')),
                ('active', models.BooleanField(default=False, verbose_name=b'Activo')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'Nombre')),
                ('file', models.ImageField(upload_to=app.models.upload_image_to, verbose_name=b'Imagen grande')),
                ('thumbnail', models.ImageField(upload_to=app.models.upload_image_to, verbose_name=b'Imagen peque\xc3\xb1a')),
                ('order', models.IntegerField(default=0, verbose_name=b'Orden')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Im\xe1genes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(verbose_name=b'Cantidad')),
                ('price', models.DecimalField(verbose_name=b'Precio', max_digits=18, decimal_places=0)),
                ('discount_price', models.DecimalField(verbose_name=b'Precio oferta', max_digits=18, decimal_places=0)),
                ('cart', models.ForeignKey(to='app.Cart')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name=b'Creado')),
                ('paid', models.DateTimeField(null=True, verbose_name=b'Pagado', blank=True)),
                ('canceled', models.BooleanField(default=False, verbose_name=b'Cancelado')),
                ('expired', models.BooleanField(default=False, verbose_name=b'Expirado')),
                ('delivered', models.DateTimeField(null=True, verbose_name=b'Enviado', blank=True)),
                ('amount', models.DecimalField(verbose_name=b'Total', max_digits=18, decimal_places=0)),
                ('payment_method', models.CharField(blank=True, max_length=2, null=True, verbose_name=b'M\xc3\xa9todo de pago', choices=[(b'TR', b'Transferencia'), (b'WP', b'Webpay'), (b'KH', b'Khipu')])),
                ('uuid', uuidfield.fields.UUIDField(verbose_name=b'uuid', unique=True, max_length=32, editable=False, blank=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'Nombre')),
                ('email', models.CharField(max_length=128, verbose_name=b'Correo electr\xc3\xb3nico', blank=True)),
                ('phone', models.CharField(max_length=64, verbose_name=b'Tel\xc3\xa9fono fijo', blank=True)),
                ('mobile', models.CharField(max_length=64, verbose_name=b'T\xc3\xa9lefono m\xc3\xb3vil', blank=True)),
                ('address0', models.CharField(max_length=256, verbose_name=b'Direcci\xc3\xb3n', blank=True)),
                ('address1', models.CharField(max_length=256, verbose_name=b'Direcci\xc3\xb3n', blank=True)),
                ('city', models.CharField(max_length=64, verbose_name=b'Ciudad', blank=True)),
                ('region', models.CharField(max_length=64, verbose_name=b'Regi\xc3\xb3n', blank=True)),
                ('country', models.CharField(max_length=64, verbose_name=b'Pa\xc3\xads', blank=True)),
                ('postal_code', models.IntegerField(null=True, verbose_name=b'C\xc3\xb3digo postal', blank=True)),
                ('numero_despacho', models.CharField(max_length=256, null=True, verbose_name=b'N\xc3\xbamero de despacho', blank=True)),
                ('comentarios', models.TextField(null=True, verbose_name=b'Comentarios', blank=True)),
                ('comentarios_interno', models.TextField(null=True, verbose_name=b'Informaci\xc3\xb3n interna', blank=True)),
                ('cart', models.ForeignKey(verbose_name=b'Carro', to='app.Cart')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, verbose_name=b'Nombre')),
                ('slug', models.SlugField(max_length=128, verbose_name=b'Slug')),
                ('shortdescription', models.CharField(max_length=128, verbose_name=b'Descripci\xc3\xb3n corta')),
                ('longdescription', models.TextField(verbose_name=b'Descripci\xc3\xb3n larga')),
                ('keywords', models.CharField(max_length=256, verbose_name=b'Palabras clave')),
                ('price', models.DecimalField(verbose_name=b'Precio', max_digits=18, decimal_places=0)),
                ('discount_price', models.DecimalField(verbose_name=b'Precio oferta', max_digits=18, decimal_places=0)),
                ('stock', models.IntegerField(default=0, verbose_name=b'Cantidad')),
                ('order', models.IntegerField(default=0, verbose_name=b'Orden')),
                ('active', models.BooleanField(default=False, verbose_name=b'Activo')),
                ('show_in_home', models.BooleanField(default=False, verbose_name=b'Destacado')),
                ('www', models.BooleanField(default=False, verbose_name=b'Mostrar en Portada')),
                ('category', models.ManyToManyField(to='app.Category', null=True, verbose_name=b'Categorias', blank=True)),
                ('related', models.ManyToManyField(to='app.Product', null=True, verbose_name=b'Relacionados', blank=True)),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=64, verbose_name=b'Tel\xc3\xa9fono fijo', blank=True)),
                ('mobile', models.CharField(max_length=64, verbose_name=b'T\xc3\xa9lefono m\xc3\xb3vil', blank=True)),
                ('address', models.CharField(max_length=256, verbose_name=b'Direcci\xc3\xb3n', blank=True)),
                ('city', models.CharField(max_length=64, verbose_name=b'Ciudad', blank=True)),
                ('region', models.CharField(max_length=64, verbose_name=b'Regi\xc3\xb3n', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfil',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(to='app.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(verbose_name=b'Producto', blank=True, to='app.Product', null=True),
            preserve_default=True,
        ),
    ]
