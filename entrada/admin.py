from entrada.models import Incoming, PaymentMethod
from django.contrib import admin

# Register your models here.

class IncomingsAdmin(admin.ModelAdmin):
    readonly_fields = ['id',]

class PaymentMethodsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Incoming)
admin.site.register(PaymentMethod)