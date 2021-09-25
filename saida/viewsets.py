from saida.serializers import CategorySerializer, DebitSerializer
from saida.models import Category, Debit
from rest_framework import viewsets


class DebitViewSet(viewsets.ModelViewSet):
    queryset = Debit.objects.all()
    serializer_class = DebitSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
