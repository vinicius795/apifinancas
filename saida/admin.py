from saida.models import Category, Debit, Place
from django.contrib import admin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class DebitAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Category)
admin.site.register(Debit)
admin.site.register(Place)