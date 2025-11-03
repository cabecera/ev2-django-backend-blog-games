from django.shortcuts import render
from django.http import HttpResponseNotFound
from .forms import ContactForm

# Vista para la página de inicio
def home(request):
    return render(request, 'core/index.html')

# Vista para la página "Acerca de"
def about(request):
    return render(request, 'core/about.html')

# Vista para la página de servicios
def services(request):
    return render(request, 'core/services.html')

# Vista para la página de contacto con formulario
def contact(request):
    # Crea instancia vacía del formulario (para GET)
    form = ContactForm()

    # Maneja envío del formulario (método POST)
    if request.method == 'POST':
        # Crea formulario con datos enviados
        form = ContactForm(request.POST)
        # Valida los datos del formulario
        if form.is_valid():
            # SOLO DISEÑO: aquí procesará el envío de los datos
            # Ej: enviar email, guardar en base de datos, etc.
            pass

    # Renderiza template con el formulario (vacío o con errores)
    return render(request, 'core/contact.html', {'form': form})

# Manejador personalizado para errores 404 (Página no encontrada)
def custom_404(request, exception):
    # Renderiza template 404 personalizado con estado HTTP 404
    return render(request, 'core/404.html', status=404)