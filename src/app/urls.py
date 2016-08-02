from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^pd/$', views.pd, name='pd'),
    url(r'^po/$', views.po, name='po'),
    url(r'^(?P<category_slug>\S+)/c/(?P<category_id>\d+)/$', views.category, name='category'),
    url(r'^productos-destacados/$', views.category_product_show_in_home, name='product_show_in_home'),
    url(r'^productos-en-oferta/$', views.category_product_discount, name='product_discount'),
    url(r'^(?P<product_slug>\S+)/p/(?P<product_id>\d+)/$', views.product, name='product'),
    url(r'^(?P<search_text>.*)/search/$', views.search, name='search'),
    url(r'^cart/get/$', views.cart_get_cart, name='cart_get'),
    url(r'^cart/add/(?P<product_id>\d+)/(?P<quantity>\d+)/$', views.cart_add_item, name='cart_add_item'),
    url(r'^cart/sub/(?P<item_id>\d+)/(?P<quantity>\d+)/$', views.cart_sub_item, name='cart_sub_item'),
    url(r'^cart/update/(?P<item_id>\d+)/(?P<quantity>\d+)/$', views.cart_update_item, name='cart_update_item'),
    url(r'^cart/delete/(?P<item_id>\d+)/$', views.cart_delete_item, name='cart_delete_item'),
    url(r'^cart/total/$', views.cart_total, name='cart_total'),
    url(r'^cart/clear/$', views.cart_clear_items, name='cart_clear_items'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^order/(?P<order_uuid>\S+)/$', views.order, name='order'),
    url(r'^contacto/$', views.contacto, name='contacto'),
)