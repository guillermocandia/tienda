from django.conf.urls import patterns, url

from solie.payments import views

urlpatterns = patterns('',
    url(r'^webpay/notify/$', views.payment_webpay_notify, name='payment_webpay_notify'),
    url(r'^webpay/error/$', views.payment_webpay_error, name='payment_webpay_error'),
    url(r'^webpay/success/$', views.payment_webpay_success, name='payment_webpay_success'),
    url(r'^webpay/(?P<order_uuid>\S+)/$', views.payment_webpay, name='payment_webpay'),
    url(r'^khipu/status/$', views.payment_khipu_status, name='payment_khipu_status'),
    url(r'^khipu/return/(?P<order_uuid>\S+)/$', views.payment_khipu_return, name='payment_khipu_return'),
    url(r'^khipu/notify/$', views.payment_khipu_notify, name='payment_khipu_notify'),
    url(r'^khipu/(?P<order_uuid>\S+)/$', views.payment_khipu, name='payment_khipu'),
    url(r'^transferencia/$', views.payment_transfer, name='payment_transfer'),   
)