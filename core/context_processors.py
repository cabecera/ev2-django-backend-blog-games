from noticias.models import Categoria, Noticia


def categorias_noticias(request):
    """
    Procesador de contexto personalizado que agrega las categorías de noticias
    y las últimas noticias a todas las plantillas.
    Útil para mostrar en navegación, footer o sidebar.
    """
    categorias = Categoria.objects.all().order_by('nombre')
    ultimas_noticias = Noticia.objects.select_related('autor', 'categoria').order_by('-created')[:5]

    return {
        'categorias_noticias': categorias,
        'ultimas_noticias': ultimas_noticias,
    }

