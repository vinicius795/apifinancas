from saida.viewsets import CategoryViewSet, DebitViewSet
from rest_framework import routers

app_name = 'saida'

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('debit', DebitViewSet)