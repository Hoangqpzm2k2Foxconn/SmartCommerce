
from django.db import models
from apps.core.models import BaseModel

class Payment(BaseModel):
    """Base payment model"""
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    status = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    
    class Meta:
        abstract = True

class Transaction(Payment):
    """Concrete transaction model"""
    reference_id = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.reference_id} - {self.amount} {self.currency}"
