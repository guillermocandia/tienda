# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from app.models import Category, Product, Image, UserProfile, Cart, Item, Order
from solie.payments.models import PaymentTransfer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from adminsortable.admin import SortableAdminMixin
from django_summernote.admin import SummernoteModelAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    
class UserAdmin(UserAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'slug', 'order', 'active']
    list_editable = ['active']

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0  

class ProductAdmin(SortableAdminMixin, SummernoteModelAdmin):
    def copy(self, request, queryset):
        l = queryset.count()
        if l == 0:
            self.message_user(request, "Debe seleccionar al menos un producto.", level=messages.ERROR)
        else:
            for q in queryset:
                n = Product()
                n.name = 'Copia de '+ q.name
                p = Product.objects.filter(name = n.name).first()
                if p:
                    n.name = n.name + ' ' + datetime.now().__str__()
                n.slug = 'copia-' + q.slug
                n.shortdescription = q.shortdescription
                n.longdescription = q.longdescription
                n.keywords = q.keywords
                n.price = q.price
                n.discount_price = q.discount_price
                n.stock = q.stock
                n.active = False
                n.show_in_home = False
                n.order = self.get_max_order() + 1
                n.save()
                category = q.category
                for c in category.all():
                    c.product_set.add(n)
            self.message_user(request, "Los productos se han copiado.")
    copy.short_description = "Copiar producto"
    
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'price', 'discount_price', 'stock', 'active', 'www']
    list_filter = ['category']
    search_fields = ['name']
    list_editable = ['active', 'www']
    inlines = [ImageInline]
    
    fieldsets = [
        (None, {
            'fields': ('name', 'slug', 'shortdescription', 'longdescription', 'stock', 'price', 'discount_price', 'www', 'active', 'category', 'related')
        }),
        ]
    actions = [copy]
    
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['name', 'file', 'thumbnail', 'product', 'order']
#     list_filter = ['product']
#     list_editable = ['product', 'order']

class ItemInline(admin.StackedInline):
    model = Item
    extra = 0

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'modified', 'checked_out']
    list_filter = ['checked_out', 'created', 'modified']
    inlines = [ItemInline]
    search_fields = ['id']
    
# class CartInline(admin.StackedInline):
#     model = Cart
#     extra = 0

class OrderAdmin(admin.ModelAdmin):
    
    def make_paid_transfer(self, request, queryset):
        l = queryset.count()
        if l == 0:
            self.message_user(request, "Debe seleccionar al menos un pedido.", level=messages.ERROR)
        else:
            for q in queryset:
                if q.paid == None:
                    payment = PaymentTransfer()
                    payment.order = q
                    payment.email = q.email
                    payment.in_process = False
                    payment.success = True
                    payment.save()
            
                    #email TODO arreglar vista gmail
                    order = payment.order
                    order.payment_method = Order.PAYMENT_METHOD_TRANSFER
                    order.paid = datetime.now()
                    order.save()
                    order.cart.update_stock()
                    
                    subject = "TIENDA: Pedido " + str(order.id) + " Pagado"
                    to = [order.email]
                    from_email = settings.EMAIL_FROM
 
                    ctx = {
                        'order' : order,
                        'request' : request    
                        }
                    message = get_template('payments/email/khipu.html').render(Context(ctx))
 
                    msg = EmailMultiAlternatives(subject, message, from_email, to)
                    msg.attach_alternative(message, "text/html")
                    msg.send()
                
                    to =settings.EMAIL_NOTIFY
                    msg2 = EmailMultiAlternatives(subject, message, from_email, to)
                    msg2.attach_alternative(message, "text/html")
                    msg2.send()
                    
            self.message_user(request, "Los pedidos han sido marcados como pagados mediante transferencia bancaria.")
    
    make_paid_transfer.short_description = "Marcar pago por transferencia"
    
    def order_link(self, item):
        return '<a href="../../../order/%s">Ver Pedido</a>' % (item.uuid)
    order_link.allow_tags = True
    order_link.short_description = 'Vista cliente'
    
    def cart_link(self, item):
        return '<a href="../cart/%s">Ver Carro</a>' % (item.cart.id)
    cart_link.allow_tags = True
    cart_link.short_description = 'Carro'
    
    list_display = ['id', 'order_link', 'cart_link', 'email', 'created', 'paid', 'payment_method', 'delivered']
    list_filter = ['created', 'paid', 'delivered', 'payment_method', 'canceled']
    readonly_fields = ('cart', 'payment_method', 'canceled', 'expired', 'amount', 'created', 'paid', 'uuid')
    #readonly_fields = ('cart', 'canceled', 'expired', 'amount', 'created', 'uuid')
    search_fields = ['id', 'email']
    fieldsets = [
        (None, {
            'fields': ('cart', 'created', 'paid', 'delivered', 'amount', 'payment_method')
        }),
        ('Datos envio', {
            'fields': ('name', 'email', 'phone', 'mobile', 'address0', 'address1', 'city', 'region', 'numero_despacho', 'comentarios', 'comentarios_interno')
        }),
        ('Información adicional', {
            'classes': ('collapse',),
            'fields': ('uuid', 'expired', 'canceled')
        })
        ]

    actions = [make_paid_transfer]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.site_title = 'TIENDA'
admin.site.site_header = 'Administración TIENDA'
