from django.contrib import admin

from .models import Autor, Categoria, Noticia


class AutorAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


class NoticiaAdmin(admin.ModelAdmin):  # Personalización admin: 8+ parámetros
    readonly_fields = ("created", "updated")  # Campos solo lectura
    list_display = ("titulo", "autor", "categoria", "created")  # Columnas visibles
    list_filter = ("categoria", "autor", "created")  # Filtros laterales
    search_fields = ("titulo", "detalle", "autor__nombre")  # Búsqueda
    ordering = ("-created",)  # Orden por fecha
    date_hierarchy = "created"  # Navegación por fechas
    list_per_page = 25  # Elementos por página
    autocomplete_fields = ["autor", "categoria"]  # Autocompletado


admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)