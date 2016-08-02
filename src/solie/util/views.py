from django.http.response import HttpResponse
from django.core import serializers
from solie.util.models import Slide

def slide(request):
    data = serializers.serialize('json', Slide.objects.filter(active = True).order_by('order'))
    return HttpResponse(data)
