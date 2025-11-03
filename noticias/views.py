from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Noticia, Autor, Categoria

def noticias(request):
    # CONSULTA INICIAL OPTIMIZADA
    # select_related evita el problema N+1 en consultas de autor y categoría
    lista_noticias = (
        Noticia.objects.select_related('autor', 'categoria')
        .all()  # Obtiene todas las noticias inicialmente
    )

    # CAPTURA DE PARÁMETROS DE FILTRO
    # Los filtros vienen por GET (en la URL)
    categoria_id = request.GET.get('categoria')  # Ej: ?categoria=2
    autor_id = request.GET.get('autor')          # Ej: ?autor=5

    # APLICACIÓN DE FILTROS
    # Filtra por categoría si se especificó
    if categoria_id:
        lista_noticias = lista_noticias.filter(categoria_id=categoria_id)

    # Filtra por autor si se especificó
    if autor_id:
        lista_noticias = lista_noticias.filter(autor_id=autor_id)

    # ORDENAMIENTO
    # Ordena por fecha de creación descendente (más recientes primero)
    lista_noticias = lista_noticias.order_by('-created')

    # PAGINACIÓN

    paginator = Paginator(lista_noticias, 5)# Divide resultados en páginas de 5 elementos cada una
    page_number = request.GET.get('page')# Obtiene número de página desde URL (ej: ?page=2)
    page_obj = paginator.get_page(page_number)# Obtiene objeto de página actual

    # DATOS PARA LOS FILTROS
    # Obtiene todas las categorías y autores para llenar los selects
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()

    # CONVERSIÓN DE PARÁMETROS PARA TEMPLATE
    # Convierte IDs a enteros para comparaciones en template
    categoria_selected = int(categoria_id) if categoria_id else None
    autor_selected = int(autor_id) if autor_id else None

    # RENDERIZADO DE LA VISTA
    return render(request, 'noticias/noticias.html', {
        'page_obj': page_obj,           # Objeto de paginación con noticias
        'categorias': categorias,       # Todas las categorías para filtro
        'autores': autores,             # Todos los autores para filtro
        'categoria_selected': categoria_selected,  # Categoría activa
        'autor_selected': autor_selected,          # Autor activo
    })