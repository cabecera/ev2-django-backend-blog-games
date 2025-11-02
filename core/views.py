from django.shortcuts import render
from django.http import HttpResponseNotFound
from .forms import ContactForm


def home(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def services(request):
    return render(request, 'core/services.html')


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass

    return render(request, 'core/contact.html', {'form': form})


def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)