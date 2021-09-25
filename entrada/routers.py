from entrada.viewsets import IncomingViewSet, PaymentMethodViewSet
from rest_framework import routers

app_name = 'entrada'

router = routers.DefaultRouter()
router.register('paymentmethod', PaymentMethodViewSet)
router.register('incomings', IncomingViewSet)