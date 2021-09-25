from django.db import models


class Category (models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)

    def __str__(self):
        return self.name


class Debit (models.Model):
    date = models.DateField()
    type = models.ManyToManyField(Category)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    place = models.ManyToManyField(Place, blank=True)
    nfe = models.CharField(max_length=44, null=True, blank=True, default="")
