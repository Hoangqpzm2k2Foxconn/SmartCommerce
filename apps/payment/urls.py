
from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.payment_home, name='home'),
    path('process/', views.process_payment, name='process'),
]
