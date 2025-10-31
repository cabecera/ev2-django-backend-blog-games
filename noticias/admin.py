from django.contrib import admin

from .models import Autor, Categoria, Noticia


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


# Registramos los modelos que existen

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Noticia)