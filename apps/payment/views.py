
from django.shortcuts import render
from django.http import JsonResponse
from .services import PaymentService

def payment_home(request):
    return render(request, 'payment/home.html', {
        'title': 'Payment Gateway'
    })

def process_payment(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
