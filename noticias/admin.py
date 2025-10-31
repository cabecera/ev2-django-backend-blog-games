from django.contrib import admin

from .models import Autor, Categoria, Noticia


class AutorAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("titulo", "autor", "categoria", "created")
    list_filter = ("categoria", "autor", "created")
    search_fields = ("titulo", "detalle", "autor__nombre")
    ordering = ("-created",)
    date_hierarchy = "created"
    list_per_page = 25
    autocomplete_fields = ["autor", "categoria"]


admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)