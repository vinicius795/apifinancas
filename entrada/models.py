from django.db import models
from django.db.models.fields import CharField

class PaymentMethod (models.Model):
    name = CharField(blank=False, null=False, max_length=255)

    def __str__(self):
        return self.name


class Incoming (models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.ManyToManyField(PaymentMethod, blank=True)
    

