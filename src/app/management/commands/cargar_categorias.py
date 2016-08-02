# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from app.models import Category
import unicodedata

class Command(BaseCommand):
    args = '<archivo_categorias>'
    help = 'Carga categorias desde archivo'

    def handle(self, *args, **options):
        archivo = args[0]
        f = open(archivo, 'r')
        l = f.readlines()
        count = 0
        for c in l:
            c = c[1:]
            c = c[:-2]
            slug = c.replace(' ', '-')
            slug = slug.replace(',', '')
            slug = slug.decode('latin-1')
            slug = unicodedata.normalize('NFKD', slug).encode('ASCII', 'ignore') 
            slug = slug.lower()
            
            category = Category()
            category.name = c
            category.slug = slug
            category.order = 0
            category.active = True
            
            try:
                category.save()
                count += 1
                self.stdout.write('Categoria %s almacenada' %  c)
            except Exception:
                self.stdout.write('Categoria %s NO almacenada' %  c)
            
        self.stdout.write('Se almacenaron %d categorias' % count)