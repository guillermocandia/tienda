from solie.util.models import Aviso

def aviso_proc(request):
    aviso = Aviso.objects.filter(active = True).last()
    return {
            'aviso': aviso
    }