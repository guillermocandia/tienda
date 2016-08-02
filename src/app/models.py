# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from uuidfield import UUIDField

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length = 64, blank = True, verbose_name = 'Teléfono fijo')
    mobile = models.CharField(max_length = 64, blank = True, verbose_name = 'Télefono móvil')
    address = models.CharField(max_length = 256, blank = True, verbose_name = 'Dirección')
    city = models.CharField(max_length = 64, blank = True, verbose_name = 'Ciudad')
    region = models.CharField(max_length = 64, blank = True, verbose_name = 'Región')
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfil'

class Category(models.Model):
    name = models.CharField(max_length = 64, blank = False, unique = True, verbose_name = 'Nombre')
    slug = models.SlugField(max_length = 64, blank = False, verbose_name = 'Slug')
    order = models.IntegerField(default = 0, verbose_name = 'Orden')
    active = models.BooleanField(default = False, verbose_name = 'Activo')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('order',)

    def __str__(self):
        return self.name;
    
    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 128, blank = False, unique = True, verbose_name = 'Nombre')
    slug = models.SlugField(max_length = 128, blank = False, verbose_name = 'Slug')
    shortdescription = models.CharField(max_length = 128, verbose_name = 'Unidad/Cantidad')
    longdescription = models.TextField(verbose_name = 'Descripción larga')
    keywords = models.CharField(max_length = 256, verbose_name = 'Palabras clave')
    price = models.DecimalField(max_digits = 18, decimal_places = 0, verbose_name = 'Precio')
    discount_price = models.DecimalField(max_digits = 18, decimal_places = 0, verbose_name = 'Precio oferta')
    stock = models.IntegerField(default = 0, verbose_name = 'Cantidad')
    order = models.IntegerField(default = 0, verbose_name = 'Orden')
    active = models.BooleanField(default = False, verbose_name = 'Activo')
    category = models.ManyToManyField(Category, blank = True, null = True, verbose_name = 'Categorias')
    related = models.ManyToManyField('self', null = True, blank = True, symmetrical = False, verbose_name = 'Relacionados')
    show_in_home = models.BooleanField(default = False, verbose_name = 'Destacado')
    www = models.BooleanField(default = False, verbose_name = 'Mostrar en Portada')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ('order',)
        
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    def first_image(self):
        return self.image_set.order_by('order').first()
    
    def have_discount(self):
        return self.discount_price > 0

def upload_image_to(instance, filename):
    from django.utils.timezone import now
    return 'media/%s_%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename.lower(),
    )

class Image(models.Model):
    name = models.CharField(max_length = 64, verbose_name = 'Nombre')
    file = models.ImageField(upload_to = upload_image_to, verbose_name = 'Imagen grande')# TODO desplegar imaganes en admin
    thumbnail = models.ImageField(upload_to = upload_image_to, verbose_name = 'Imagen pequeña')
    product = models.ForeignKey(Product, blank = True, null = True, verbose_name = 'Producto')
    order = models.IntegerField(default = 0, verbose_name = 'Orden')
    
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
        
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, verbose_name = 'Usuario')

    created = models.DateTimeField(verbose_name = 'Creado')
    modified = models.DateTimeField(verbose_name = 'Modificado')
    checked_out = models.BooleanField(default = False, verbose_name = 'Confirmado')
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    
    def get_items(self):
        return self.item_set.all()
    
    def add_item(self, product_id, quantity):
        item = Item.objects.filter(product_id = product_id, cart = self.pk).first()
        product = Product.objects.get(pk = product_id)
        if item:
            item.quantity += int(quantity)
        else :
            item = Item()
            item.cart = self
            item.product = product
            item.quantity = quantity
            item.price = product.price
            item.discount_price = product.discount_price
        if int(item.quantity) > int(product.stock):
            return False
        if product.active == False:
            return False
        
        item.save()
        self.modified = datetime.now()
        self.save()
        return True
    
    def sub_item(self, item_id, quantity):
        item = Item.objects.get(pk = item_id)
        if item.quantity == 0:
            return
        if item.quantity - int(quantity) < 1:
            item.quantity = 1   
        else:
            item.quantity -= int(quantity)
        item.save()
        self.modified = datetime.now()
        self.save() 
    
    def update_item(self, item_id, quantity):
        item = Item.objects.get(pk = item_id)
        product = Product.objects.get(pk = item.product.id)
        item.quantity = quantity
        if int(item.quantity) > int(product.stock):
            return False
        item.save()
        self.modified = datetime.now()
        self.save()
        return True
    
    def delete_item(self, item_id):
        item = Item.objects.get(pk = item_id)
        item.delete()
        self.modified = datetime.now()
        self.save()
        
    def clear_items(self):
        for i in self.item_set.all():
            i.delete()
        self.modified = datetime.now()
        self.save()
    
    def get_total(self):
        t = 0
        for i in self.item_set.all():
            if i.discount_price > 0:
                t += i.discount_price * i.quantity
            else:
                t += i.price * i.quantity
        return t
    
    def __str__(self):
        return 'Carro ' + str(self.id)
    
    def update_stock(self):
        items = Item.objects.filter(cart = self.pk)
        for item in items:
            item.product.stock -= item.quantity
            item.product.save()
    
class Item(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(verbose_name = 'Cantidad')
    price = models.DecimalField(max_digits = 18, decimal_places = 0, verbose_name = 'Precio')
    discount_price = models.DecimalField(max_digits = 18, decimal_places = 0, verbose_name = 'Precio oferta')
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
    
    def __str__(self):
        return self.product.name
    
    def __unicode__(self):
        return self.product.name
        
class Order(models.Model):
    PAYMENT_METHOD_TRANSFER = 'TR'
    PAYMENT_METHOD_WEBPAY = 'WP'
    PAYMENT_METHOD_KHIPU = 'KH'
    
    PAYMENT_METHOD_CHOICES = (
        (PAYMENT_METHOD_TRANSFER , 'Transferencia'),
        (PAYMENT_METHOD_WEBPAY , 'Webpay'),
        (PAYMENT_METHOD_KHIPU , 'Khipu')
    )
    
    cart = models.ForeignKey(Cart, verbose_name = 'Carro')
    created = models.DateTimeField(verbose_name = 'Creado')
    paid = models.DateTimeField(null = True, blank = True, verbose_name = 'Pagado')
    canceled = models.BooleanField(default = False, verbose_name = 'Cancelado')
    expired = models.BooleanField(default = False, verbose_name = 'Expirado')
    delivered = models.DateTimeField(null = True, blank = True, verbose_name = 'Enviado')
    amount = models.DecimalField(max_digits = 18, decimal_places = 0, verbose_name = 'Total')
    payment_method = models.CharField(max_length = 2, null = True, blank = True, choices = PAYMENT_METHOD_CHOICES ,verbose_name = 'Método de pago')
    uuid = UUIDField(auto = True, verbose_name = 'uuid')
    
    name = models.CharField(max_length = 256, verbose_name = 'Nombre')
    email = models.CharField(max_length = 128, blank = True, verbose_name = 'Correo electrónico')
    phone = models.CharField(max_length = 64, blank = True, verbose_name = 'Teléfono fijo')
    mobile = models.CharField(max_length = 64, blank = True, verbose_name = 'Télefono móvil')
    address0 = models.CharField(max_length = 256, blank = True, verbose_name = 'Dirección')
    address1 = models.CharField(max_length = 256, blank = True, verbose_name = 'Dirección')
    city = models.CharField(max_length = 64, blank = True, verbose_name = 'Ciudad')
    region = models.CharField(max_length = 64, blank = True, verbose_name = 'Región')
    country = models.CharField(max_length = 64, blank = True, verbose_name = 'País')
    postal_code = models.IntegerField(null = True, blank = True, verbose_name = 'Código postal')
    
    #información extra
    numero_despacho = models.CharField(max_length = 256, null = True, blank = True, verbose_name = 'Número de despacho')
    comentarios = models.TextField(null = True, blank = True, verbose_name = 'Comentarios')
    comentarios_interno = models.TextField(null = True, blank = True, verbose_name = 'Información interna')  
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return 'Pedido ' + str(self.id)
