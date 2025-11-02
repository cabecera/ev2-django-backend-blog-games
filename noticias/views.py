from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Noticia, Autor, Categoria

def noticias(request):
    lista_noticias = (
        Noticia.objects.select_related('autor', 'categoria')
        .all()
    )

    categoria_id = request.GET.get('categoria')
    autor_id = request.GET.get('autor')

    if categoria_id:
        lista_noticias = lista_noticias.filter(categoria_id=categoria_id)

    if autor_id:
        lista_noticias = lista_noticias.filter(autor_id=autor_id)

    lista_noticias = lista_noticias.order_by('-created')

    paginator = Paginator(lista_noticias, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()
    autores = Autor.objects.all()

    categoria_selected = int(categoria_id) if categoria_id else None
    autor_selected = int(autor_id) if autor_id else None

    return render(request, 'noticias/noticias.html', {
        'page_obj': page_obj,
        'categorias': categorias,
        'autores': autores,
        'categoria_selected': categoria_selected,
        'autor_selected': autor_selected,
    })
