# noticias/models.py - TU NUEVO MODELO
from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    detalle = models.TextField()
    autor = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    # El método str sirve para que el admin muestre el título en lugar de “Noticia object”.

