from datetime import datetime
import time
import hmac
import hashlib
import requests
import os
import sys
from django.shortcuts import render
from django.template import RequestContext
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.utils.http import urlencode
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponseForbidden

from app.models import Order
from solie.payments.models import Payment, PaymentTransfer, PaymentKhipu, PaymentWebpay
from django.conf import settings
from array import array

def payment_webpay(request, order_uuid):
    pass


@csrf_exempt
def payment_webpay_notify(request):
    pass

@csrf_exempt
def payment_webpay_success(request):
    pass

@csrf_exempt
def payment_webpay_error(request):
    pass

def payment_khipu(request, order_uuid):
    pass

def payment_khipu_return(request, order_uuid):
    pass

@csrf_exempt
def payment_khipu_notify(request):
    pass

@staff_member_required
def payment_khipu_status(request):
    pass

def payment_transfer(request):     
    return render(request, 'payments/transfer.html', 
            {},
            context_instance = RequestContext(request, processors = [])
        )

