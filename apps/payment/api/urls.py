
from django.urls import path
from . import views

app_name = 'payment-api'

urlpatterns = [
    path('create/', views.CreatePaymentView.as_view(), name='create'),
    path('verify/<str:payment_id>/', views.VerifyPaymentView.as_view(), name='verify'),
]
