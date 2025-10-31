from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    return render(request, 'core/contact.html')


def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)