from rest_framework import serializers

from .models import BusinessOrder

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessOrder
        fields =[
            'billdate1',
            'shopcode',
            'goodscode',
            'qty',
            'amount',
            'vipcardno',
            'brand',
            'holiday',
            'orderamount',
            'orderqty',
            'amounttag',
        ]