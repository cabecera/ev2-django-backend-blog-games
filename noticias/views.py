from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Noticia

def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('-created')  # Orden descendente por fecha
    paginator = Paginator(lista_noticias, 5)  # 5 noticias por página

    page_number = request.GET.get('page')  # Captura el número de página de la URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'noticias/noticias.html', {'page_obj': page_obj})
