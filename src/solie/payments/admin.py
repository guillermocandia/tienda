from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from solie.payments.models import Payment, PaymentTransfer, PaymentKhipu, PaymentWebpay
from app.models import Order

class PaymentTransferAdmin(PolymorphicChildModelAdmin):
    base_model = Payment
    
class PaymentKhipuAdmin(PolymorphicChildModelAdmin):
    base_model = Payment
   
class PaymentWebpayAdmin(PolymorphicChildModelAdmin):
    base_model = Payment
    
class PaymentAdmin(PolymorphicParentModelAdmin):
    base_model = Payment
    child_models = (
        (PaymentTransfer, PaymentTransferAdmin),
        (PaymentKhipu, PaymentKhipuAdmin),
        (PaymentWebpay, PaymentWebpayAdmin),
    )

admin.site.register(Payment, PaymentAdmin)
