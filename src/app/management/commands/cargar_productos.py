# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from app.models import Category, Product
import unicodedata

class Command(BaseCommand):
    args = '<archivo_productos>'
    help = 'Carga productos desde archivo'

    def handle(self, *args, **options):
        archivo = args[0]
        f = open(archivo, 'r')
        l = f.readlines()
        count = 0
        for c in l:
            name, longdescription, shortdescription, price, category = c.split('#')
            
            name = name[1:-1]
            name = name.decode('utf-8')
            
            slug = name.replace(' ', '-')
            slug = slug.replace(',', '')
            slug = slug.replace(':', '')
            slug = unicodedata.normalize('NFKD', slug).encode('ASCII', 'ignore') 
            slug = slug.lower()
            
            shortdescription = shortdescription[1:-1]
            shortdescription = shortdescription.decode('utf-8')
            
            longdescription = longdescription[1:-1]
            longdescription = longdescription.decode('utf-8')
            
            keywords = slug.replace('-', ',')
            
            price = price[1:-1]
            price = int(price)
            
            discount_price = 0
            
            stock = 1000
            
            order = 0
            
            active = True
            
            category = category[1:-2]
            category = Category.objects.get(name = category)
            
            show_in_home = False
            
            product = Product()
            product.name = name
            product.slug = slug
            product.shortdescription = shortdescription
            product.longdescription = longdescription
            product.keywords = keywords
            product.price = price
            product.discount_price = discount_price
            product.stock = stock
            product.order = order
            product.active = active
            product.show_in_home = show_in_home
             
            try:
                product.save()
                category.product_set.add(product)
                count += 1
                self.stdout.write('Producto %s almacenado' %  product.name)
            except Exception:
                self.stdout.write('Producto %s NO almacenado' %  product.name)
            
        self.stdout.write('Se almacenaron %d productos' % count)