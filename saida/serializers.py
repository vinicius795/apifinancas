from saida.models import Category, Debit, Place
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= Category
        fields = ['id','name']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [ 'id', 'name'] 

class DebitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Debit
        fields = ['id', "date", "type", 'value', 'place', 'nfe']