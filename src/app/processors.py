from app.models import Category

def category_list_proc(request):
    category_list = Category.objects.filter(active = True).order_by('order')
    return {
            'category_list': category_list
    }