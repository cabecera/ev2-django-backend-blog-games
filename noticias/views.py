from django.shortcuts import render
from .models import Noticia

# Create your views here.
def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/noticias.html', {'noticias': noticias})
#Esto obtiene todas las noticias de la base de datos y las envía al template noticias.html.


