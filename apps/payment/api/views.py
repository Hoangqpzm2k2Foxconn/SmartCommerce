
from rest_framework import generics
from rest_framework.response import Response
from ..models import Transaction
from .serializers import TransactionSerializer

class CreatePaymentView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

class VerifyPaymentView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'payment_id'
