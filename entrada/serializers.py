from entrada.models import Incoming, PaymentMethod
from rest_framework import serializers


class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = [
            'id',
            'name',
        ]

class IncomingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incoming
        fields = [
            'id',
            'date',
            'type',
            'amount',
        ]
