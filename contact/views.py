from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            subject = f"Contacto desde web: {d['name']}"
            body = f"De: {d['email']}\n\n{d['message']}"
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
