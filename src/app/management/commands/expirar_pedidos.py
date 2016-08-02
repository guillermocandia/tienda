# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from app.models import Order
from datetime import datetime, timedelta
from django.core.mail import EmailMessage
from django.conf import settings

class Command(BaseCommand):
    args = '<dias>'
    help = 'Expira Pedidos con mas de X dias'

    def handle(self, *args, **options):
        dias = args[0]
        fecha = datetime.now()
        dif = timedelta(days = int(dias))
        fecha = fecha - dif
        print fecha
        orders = Order.objects.filter(payment_method = None, created__lte = fecha, expired = False)       
        message = ''
        for order in orders:
            order.expired = True
            order.save()
            message += order.__str__() + ' creado el ' + order.created.__str__() + '\n'
        
        message += 'Se expiraron %d pedidos' % orders.count()
        subject = "TIENDA: Pedidos expirados el " + datetime.now().__str__()
        to = [settings.EMAIL_ADMIN]
        from_email = 'contacto@ejemplo.com'
        msg = EmailMessage(subject, message, from_email, to)        
        msg.send()