# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from allauth.account.views import confirm_email

class OrderForm(forms.Form):
    name = forms.CharField(max_length = 256, required = True, label = 'Nombre')
    email = forms.CharField(required = True, validators=[validate_email], label = 'Correo electrónico')
    confirm_email = forms.CharField(required = True, validators=[validate_email], label = 'Repita correo electrónico')
    phone = forms.CharField(max_length = 64, required = False, label = 'Teléfono fijo')
    mobile = forms.CharField(max_length = 64, required = False, label = 'Télefono móvil')
    address0 = forms.CharField(max_length = 128, required = True, label = 'Dirección de entrega')
    #address1 = forms.CharField(max_length = 128, required = False, label = 'Dirección de entrega 2')
    city = forms.CharField(max_length = 64,required = True, label = 'Comuna')
    region = forms.CharField(max_length = 64, required = True, label = 'Región')
#    postal_code = forms.CharField(max_length = 32 ,required = False, label = 'Código postal')
#    country = forms.CharField(max_length = 64, required = True, label = 'País')

    def clean_phone(self):
        if (self['phone'].value().strip() == '' and
            self['mobile'].value().strip() == ''):
            raise ValidationError("Debe ingresar a lo menos un télefono de contacto.")
        return self.cleaned_data.get('phone')

    def clean_email(self):
        if (self['email'].value().strip() !=
            self['confirm_email'].value().strip()):
            raise ValidationError("Correo electrónico debe coincidir")
        return self.cleaned_data.get('email')

class ContactoForm(forms.Form):
    name = forms.CharField(max_length = 256, required = True, label = 'Nombre')
    email = forms.CharField(required = True, validators=[validate_email], label = 'Correo electrónico')
    msg = forms.CharField(widget=forms.Textarea, required = True, label = 'Mensaje')
    