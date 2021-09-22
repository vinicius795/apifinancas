from django.db import models
from django.db.models.fields import CharField

class Payment_method (models.Model):
    name = CharField(blank=False, null=False, max_length=255)

class Incomings (models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.ManyToManyField(Payment_method, null=True, blank=True)
    

