# -*- coding: utf-8 -*-
from django.db import models

class Aviso(models.Model):
    mensaje = models.CharField(max_length = 128, blank = True, verbose_name = 'Mensaje')
    active = models.BooleanField(default = False, verbose_name = 'Activo')
    
    class Meta:
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'

    def __str__(self):
        return self.mensaje;
    
    def __unicode__(self):
        return self.mensaje
 
def upload_image_to(instance, filename):
    return 'media/slide/%s' % (
        filename.lower(),
    ) 
 
class Slide(models.Model):
    file = models.ImageField(upload_to = upload_image_to, verbose_name = 'Imagen')
    titulo = models.CharField(max_length = 256, blank = True, verbose_name = 'Titulo')
    mensaje = models.TextField(blank = True, verbose_name = 'Mensaje')
    active = models.BooleanField(default = False, verbose_name = 'Activo')
    enlace = models.CharField(max_length = 256, verbose_name = 'Enlace')
    order = models.IntegerField(default = 0, verbose_name = 'Orden')
    
    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'
        ordering = ('order',)

    def __str__(self):
        return self.titulo;
    
    def __unicode__(self):
        return self.titulo     