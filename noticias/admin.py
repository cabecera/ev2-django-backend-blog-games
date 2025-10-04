from django.contrib import admin

#Ahora se pueden crear noticias desde el panel admin.
from .models import Noticia


# Register your models here.
admin.site.register(Noticia)
