from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.mail import send_mail
from .forms import ContactForm
import requests

# Vista para la página de inicio
def home(request):
    return render(request, 'core/index.html')

# Vista para la página "Acerca de"
def about(request):
    return render(request, 'core/about.html')

# Vista para la página de servicios
def services(request):
    return render(request, 'core/services.html')

# Vista para la página de contacto con formulario y envío a Mailtrap
def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            tipo = form.cleaned_data['tipo_consulta'] or "No especificado"

            cuerpo = f"""
Nuevo mensaje de contacto desde GameHub:

Nombre: {nombre}
Correo: {email}
Asunto: {asunto}
Tipo de consulta: {tipo}

Mensaje:
{mensaje}
"""

            # Enviar correo a Mailtrap
            send_mail(
                subject=f"[GameHub] {asunto}",
                message=cuerpo,
                from_email="test@example.com",  # No importa, Mailtrap lo recibe igual
                recipient_list=["test@example.com"],  # Se queda en Mailtrap
                fail_silently=False,
            )

            return render(request, 'core/contact_success.html')

    return render(request, 'core/contact.html', {'form': form})

# Vista personalizada 404
def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)

def api_consumer_products(request):
    try:
        response = requests.get('http://127.0.0.1:8000/api/products/')
        products = response.json()
    except:
        products = []

    return render(request, 'core/api_consumer_products.html', {'products': products})