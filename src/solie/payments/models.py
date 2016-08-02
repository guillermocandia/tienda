# -*- coding: utf-8 -*-
from django.db import models
from polymorphic import PolymorphicModel
from app.models import Order

class Payment(PolymorphicModel):
    order = models.ForeignKey(Order)
    in_process = models.BooleanField(default = False, verbose_name = 'En proceso')
    success = models.BooleanField(default = False, verbose_name = 'Exito')
    email = models.CharField(max_length = 128, blank = True, verbose_name = 'Correo electrónico')
    
    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
                
class PaymentTransfer(Payment):
    transfer_extra = models.CharField(max_length = 255, blank = True, null = True, verbose_name = 'Información extra')

    class Meta:
        verbose_name = 'Pago por transferencia'
        verbose_name_plural = 'Pagos por transferencia'

class PaymentKhipu(Payment):
    khipu_extra = models.CharField(max_length = 255, blank = True, null = True, verbose_name = 'Información extra')
    
    khipu_id = models.CharField(max_length = 255, blank = True, null = True, verbose_name = 'id')
    khipu_bill_id = models.CharField(max_length = 128, blank = True, null = True, verbose_name = 'bill-id')
    khipu_url = models.CharField(max_length = 255, blank = True, null = True, verbose_name = 'url')
    khipu_manual_url = models.CharField(max_length = 255, blank = True, null = True, verbose_name = 'manual-url')
    khipu_mobile_url = models.CharField(max_length = 255, blank = True, null = True, verbose_name = 'mobile-url')
    khipu_ready_for_terminal = models.BooleanField(default = False, verbose_name = 'ready-for-terminal')

    class Meta:
        verbose_name = 'Pago por Khipu'
        verbose_name_plural = 'Pagos por Khipu'

class PaymentWebpay(Payment):
    webpay_extra = models.CharField(max_length = 255, blank = True, null = True, verbose_name = 'Información extra')
     
    TBK_MONTO = models.IntegerField(null = True, verbose_name = 'TBK_MONTO')
    TBK_CODIGO_AUTORIZACION = models.IntegerField(null = True, verbose_name = 'TBK_CODIGO_AUTORIZACION')
    TBK_FECHA_CONTABLE = models.IntegerField(null = True, verbose_name = 'TBK_FECHA_CONTABLE')
    TBK_VCI = models.CharField(max_length = 3, null = True, verbose_name = 'TBK_VCI')
    TBK_ORDEN_COMPRA = models.CharField(null = True, max_length = 255, verbose_name = 'TBK_ORDEN_COMPRA')
    #TBK_MAC = 9c17a1a45d8359ab51e84e1c1ee67dea6cd8ad516838b4a121ff44dec8b86fbc613fa99f6c385ed74d2e588b5d4d51fff3124036fb4532b464bc6dfe6b887a456c96e493b250fbfb5c74473b6c6b885a47afb2951d7383d41614c268c5419b37ccdb5fafc8c2409b6a69f88191ae35da047fdb18aeff0d6b9c5983bd9b8b449ba724deb34a4f7c9ea8374803c8940667dfbd0f9c330b5dcf3c5c22b055ab07e84b50a794e5d04727367e1479bdd4b6a284f2679ee44a5a20df14c1fea04975ee0d2793da5f95c45ad8793848e931a83a6361a0c5deb4801ee9514c992c7043f14bb96db003990263e1c387cf1556ce9cd731274d0679bcf918f00cc52bea013d8c6be569738b22467e4cc7d24ca9aac0d6780f50a8c43088a700835ecddcedfa1bc85c01ca862a153b648a84ccb531437427b4d1ca63d509c4b1bd9c6c4cd62509c9cdcc45d3d637515b46da671a1f92e74236c29d3fcc699a15e38d6c99cda4c77f7a612be17fea47db67a4b775e3b2066393df9347d27e177c8845a9115684dcffe703f9fb12282467b43867c6fa6bf6e402af8af4f7c2c3a2f72d1c590870cd2ad251e7c676eb22ea57a88f45e371338bd6fa4484da4dceea11def484815662b3518df118784a06041a39f6465528e5fe3741b58c6e6b9b4fdc06e2b2fb2bc475060926eccf182402144e78866081ffe7e0bebfddee23395ee69c85aef632
    TBK_NUMERO_CUOTAS = models.IntegerField(null = True, verbose_name = 'TBK_NUMERO_CUOTAS')
    TBK_FECHA_TRANSACCION = models.IntegerField(null = True, verbose_name = 'TBK_FECHA_TRANSACCION')
    TBK_RESPUESTA = models.IntegerField(null = True, verbose_name = 'TBK_RESPUESTA')
    TBK_ID_SESION = models.CharField(null = True, max_length = 255, verbose_name = 'TBK_ID_SESION')
    TBK_FINAL_NUMERO_TARJETA = models.IntegerField(null = True, verbose_name = 'TBK_FINAL_NUMERO_TARJETA')
    TBK_TIPO_TRANSACCION = models.CharField(null = True, max_length = 255, verbose_name = 'TBK_TIPO_TRANSACCION')
    TBK_ID_TRANSACCION = models.IntegerField(null = True, verbose_name = 'TBK_ID_TRANSACCION')
    TBK_HORA_TRANSACCION = models.IntegerField(null = True, verbose_name = 'TBK_HORA_TRANSACCION')
    TBK_TIPO_PAGO = models.CharField(null = True, max_length = 255, verbose_name = 'TBK_TIPO_PAGO')
     
     
    class Meta:
        verbose_name = 'Pago por Webpay'
        verbose_name_plural = 'Pagos por Webpay'   
    