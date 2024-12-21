
from django.db import models
from apps.core.models import BaseModel
from apps.payment.models import Payment

class Software(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    version = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} v{self.version}"

class SoftwarePurchase(Payment):
    software = models.ForeignKey('Software', on_delete=models.CASCADE)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    license_key = models.CharField(max_length=100)
