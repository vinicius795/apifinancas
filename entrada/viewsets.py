from entrada.serializers import IncomingSerializer, PaymentMethodSerializer
from entrada.models import Incoming, PaymentMethod
from rest_framework import viewsets

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class IncomingViewSet(viewsets.ModelViewSet):
    queryset = Incoming.objects.all()
    serializer_class = IncomingSerializer