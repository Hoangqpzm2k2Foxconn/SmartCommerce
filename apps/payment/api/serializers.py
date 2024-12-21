
from rest_framework import serializers
from ..models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'currency', 'status', 'payment_method', 'reference_id']
