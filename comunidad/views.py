from django.shortcuts import render

# Create your views here.
from .models import Comunidad

def comunidad(request):
    comunidades = Comunidad.objects.all().order_by('-created')  # ✅ Ordenar por fecha
    return render(request, 'comunidad/comunidad.html', {'comunidades': comunidades})