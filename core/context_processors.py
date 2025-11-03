# Procesador de contexto personalizado para noticias
def categorias_noticias(request):
    try:
        # Importación dentro del try para evitar errores circulares
        from noticias.models import Categoria, Noticia

        # Obtiene todas las categorías ordenadas alfabéticamente
        categorias = list(Categoria.objects.all().order_by('nombre'))

        # Obtiene las 5 noticias más recientes con relaciones optimizadas
        ultimas_noticias = list(Noticia.objects.select_related('autor', 'categoria').order_by('-created')[:5])

        # Retorna diccionario con datos para todos los templates
        return {
            'categorias_noticias': categorias,  # Lista de categorías disponibles
            'ultimas_noticias': ultimas_noticias,  # Últimas 5 noticias ordenadas por fecha descendente
        }

    except Exception:
        # En caso de error (ej: tablas no creadas), retorna diccionarios vacíos
        return {
            'categorias_noticias': [],
            'ultimas_noticias': [],
        }