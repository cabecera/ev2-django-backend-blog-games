from django.shortcuts import render

def list_products_view(request):
    return render(request, 'consumer/list_products.html')
