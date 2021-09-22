from django.db import models


class Category (models.Model):
    name = models.CharField(blank=False, null=False)


class Debits (models.Model):
    date = models.DateField()
    type = models.ManyToManyField(Category)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    place = models.TextField(null=True, blank=True, default="")
    nfe = models.CharField(max_length=44, null=True, blank=True, default="")
