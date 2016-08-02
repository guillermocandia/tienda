from datetime import datetime
from django.shortcuts import render
from django.template import RequestContext
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.decorators.cache import never_cache
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

from app.models import Product, Category, Cart, Order
from app.forms import OrderForm, ContactoForm
from django.conf import settings
   
def product_home_list_proc(request):
    product_home_list = Product.objects.filter(active = True, show_in_home = True).order_by('order')
    return {
            'product_home_list' : product_home_list
    }
    
def product_discount_list_proc(request):
    product_discount_list = Product.objects.filter(active = True, discount_price__gt = 0).order_by('order')
    return {
            'product_discount_list' : product_discount_list
    }

def index(request):
    product_list = Product.objects.filter(active = True).order_by('order')
    return render(request, 'app/index.html',
                {'product_list' : product_list},
                context_instance = RequestContext(request, processors = [])
            )
    
def category(request, category_id, category_slug):
    try:
        category = Category.objects.get(id = category_id, slug = category_slug)
    except Category.DoesNotExist:
        raise Http404
    product_list = Product.objects.filter(active = True, category = category_id).order_by('order')
    return render(request, 'app/category.html', 
                {'product_list' : product_list,
                 'category_name' : category.name},
                context_instance = RequestContext(request, processors = [])
            )

def category_product_discount(request):
    product_discount_list = Product.objects.filter(active = True, discount_price__gt = 0).order_by('order')
    return render(request, 'app/category.html', 
                {'product_list' : product_discount_list,
                 'category_name' : 'PRODUCTOS EN OFERTA'},
                context_instance = RequestContext(request, processors = [])
            )

def category_product_show_in_home(request):
    product_home_list = Product.objects.filter(active = True, show_in_home = True).order_by('order')
    return render(request, 'app/category.html', 
                {'product_list' : product_home_list,
                 'category_name' : 'PRODUCTOS DESTACADOS'},
                context_instance = RequestContext(request, processors = [])
            )

def product(request, product_id, product_slug):
    try:
        product = Product.objects.get(id = product_id, slug = product_slug)
    except Product.DoesNotExist:
        raise Http404
    
    if request.is_ajax():
        return render(request, 'app/product.html',
                    {'product' : product},
                    context_instance = RequestContext(request, processors = [])
                )
    else: 
        return render(request, 'app/product_detail.html',
                    {'product' : product},
                    context_instance = RequestContext(request, processors = [])
                )

def search(request, search_text):
    word_list = search_text.split();
    product_list = Product.objects.filter(active = True).order_by('order')
    for word in word_list:
        word = word.strip()
        if word == '':
            continue
        product_list = product_list.filter(Q(name__icontains = word)
                                            |Q(shortdescription__icontains = word)
                                            |Q(longdescription__icontains = word)
                                            |Q(keywords__icontains = word))
    return render(request, 'app/search.html', 
                {'product_list' : product_list,
                 'search_text' : search_text},
                context_instance = RequestContext(request, processors = [])
            )

def cart_get_cart(request):
    cart_id = request.session.get('cart_id')
    if(cart_id):
        cart = Cart.objects.get(pk = cart_id)
    else:
        cart = None
    
    return render(request, 'app/cart.html', 
                {'cart' : cart},
                context_instance = RequestContext(request, processors = [])
            )

def cart_add_item(request, product_id, quantity):
    cart_id = request.session.get('cart_id')
    if(cart_id):
        cart = Cart.objects.get(pk = cart_id)
        cart.modified = datetime.now()
    else:
        cart = Cart()
        cart.created = datetime.now()
        cart.modified = datetime.now()
        cart.save()
        request.session['cart_id'] = cart.id             
    if cart.add_item(product_id, quantity):
        return HttpResponse('true')
    else:
        return HttpResponse('false')

def cart_sub_item(request, item_id, quantity):
    cart_id = request.session.get('cart_id')
    if(cart_id):
        cart = Cart.objects.get(pk = cart_id)
        cart.sub_item(item_id, quantity)
    else:
        pass 
    return HttpResponse('true')
    
def cart_update_item(request, item_id, quantity):
    cart_id = request.session.get('cart_id')
    if(cart_id):
        cart = Cart.objects.get(pk = cart_id)
        if cart.update_item(item_id, quantity):
            return HttpResponse('true')
        else:
            return HttpResponse('false')
    else:
        pass 
    return HttpResponse('false')

def cart_delete_item(request, item_id):
    cart_id = request.session.get('cart_id')
    if(cart_id):
        cart = Cart.objects.get(pk = cart_id)
        cart.delete_item(item_id)
    else:
        pass
    return HttpResponse('true')

def cart_total(request):
    cart_id = request.session.get('cart_id')
    if(cart_id):
        cart = Cart.objects.get(pk = cart_id)
        return HttpResponse(cart.get_total())
    else:
        return HttpResponse('false')
    
def cart_clear_items(request):
    pass

@never_cache
def checkout(request):
    cart_id = request.session.get('cart_id')
    if(cart_id):
        cart = Cart.objects.get(pk = cart_id)
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                order = Order()
                order.name = form.cleaned_data['name']
                order.email = form.cleaned_data['email']
                order.phone = form.cleaned_data['phone']
                order.mobile = form.cleaned_data['mobile']
                order.address0 = form.cleaned_data['address0']
                #order.address1 = form.cleaned_data['address1']
                order.city = form.cleaned_data['city']
                order.region = form.cleaned_data['region']
#                order.country = form.cleaned_data['country']
                order.country = 'Chile'
                order.postal_code = None
                               
                order.cart = cart
                order.amount = cart.get_total()
                order.created = datetime.now()
                order.paid = None
                order.delivered = None
                order.payment_method = None
                order.save()
                
                cart.checked_out = True
                cart.save()
                
                request.session['cart_id'] = None
                
                #email TODO arreglar vista gmail
                subject = "TIENDA: Pedido " + str(order.id) 
                to = [order.email]
                from_email = settings.EMAIL_FROM

                ctx = {
                    'order' : order,
                    'request' : request    
                }
                message = get_template('app/email/order.html').render(Context(ctx))

                msg = EmailMultiAlternatives(subject, message, from_email, to)
                msg.attach_alternative(message, "text/html")
                msg.send()
                
                to = settings.EMAIL_NOTIFY
                msg2 = EmailMultiAlternatives(subject, message, from_email, to)
                msg2.attach_alternative(message, "text/html")
                msg2.send()
               
                return HttpResponseRedirect(reverse('app.views.order', args=(order.uuid,)))
        else:
            form = OrderForm()
    else:
        cart = None
        form = None
    
    return render(request, 'app/checkout.html', 
                {'cart' : cart,
                 'form' : form},
                context_instance = RequestContext(request, processors = [])
            )

def order(request, order_uuid):
    order = Order.objects.filter(uuid = order_uuid).first()
    
    return render(request, 'app/order.html', 
                {'order' : order},
                context_instance = RequestContext(request, processors = [])
            )

@csrf_exempt
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['msg']
                                
            subject = "TIENDA: mensaje de contacto"
            to = ['info@ejemplo.com']
            from_email = 'info@ejemplo.com'
            ctx = {
                'name' : name,
                'email' : email,
                'msg' : msg    
            }
            message = get_template('app/email/contacto.html').render(Context(ctx))

            msg = EmailMultiAlternatives(subject, message, from_email, to)
            msg.attach_alternative(message, "text/html")
            msg.send()
               
            return HttpResponse('Mensaje enviado')
        #else:
        #   form = ContactoForm()
    else:
        form = ContactoForm()
    
    return render(request, 'app/contacto.html', 
                {'form' : form},
                context_instance = RequestContext(request, processors = [])
            )
    
def pd(request):
    product_home_list = Product.objects.filter(active = True, show_in_home = True).order_by('order')
    return render(request, 'app/pd.html', 
                {'product_list' : product_home_list},
                context_instance = RequestContext(request, processors = [])
            )
    
def po(request):
    product_list = Product.objects.filter(active = True, www = True).order_by('order')[:4]
    return render(request, 'app/po.html', 
                {'product_list' : product_list},
                context_instance = RequestContext(request, processors = [])
            )