
from django.shortcuts import render
from .models import Software

def software_list(request):
    products = Software.objects.all()
    return render(request, 'marketplace/list.html', {
        'products': products,
        'title': 'Software Products'
    })

def software_detail(request, pk):
    product = Software.objects.get(pk=pk)
    return render(request, 'marketplace/detail.html', {
        'product': product,
        'title': product.name
    })
