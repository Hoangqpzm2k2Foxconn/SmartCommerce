
from django.db import models
from apps.core.models import BaseModel
from apps.payment.models import Payment

class Course(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title

class CoursePayment(Payment):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
