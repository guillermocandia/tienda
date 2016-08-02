from django.contrib import admin, messages
from solie.util.models import Aviso, Slide
from adminsortable.admin import SortableAdminMixin
from datetime import datetime

class SlideAdmin(SortableAdminMixin, admin.ModelAdmin):

    def copy(self, request, queryset):
        l = queryset.count()
        if l != 1:
            self.message_user(request, "Debe seleccionar uno.", level=messages.ERROR)
        else:
            for q in queryset:
                n = Slide()
                n.titulo = 'Copia de '+ q.titulo
                p = Slide.objects.filter(titulo = n.titulo).first()
                if p:
                    n.titulo = n.titulo + ' ' + datetime.now().__str__()
                n.file = q.file
                n.mensaje = q.mensaje
                n.enlace = q.enlace
                n.active = False
                n.order = self.get_max_order() + 1
                n.save()
        self.message_user(request, "Slide copiado.")
    copy.short_description = "Copiar Slide"
    
    actions = [copy]

admin.site.register(Aviso)
admin.site.register(Slide, SlideAdmin)