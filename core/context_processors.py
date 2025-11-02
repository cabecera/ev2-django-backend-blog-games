def categorias_noticias(request):  # Procesador de contexto personalizado
    try:
        from noticias.models import Categoria, Noticia

        categorias = list(Categoria.objects.all().order_by('nombre'))  # Todas las categorías
        ultimas_noticias = list(Noticia.objects.select_related('autor', 'categoria').order_by('-created')[:5])  # Últimas 5 noticias

        return {
            'categorias_noticias': categorias,
            'ultimas_noticias': ultimas_noticias,
        }
    except Exception:
        return {
            'categorias_noticias': [],
            'ultimas_noticias': [],
        }

