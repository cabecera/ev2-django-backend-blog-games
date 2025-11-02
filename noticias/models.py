# noticias/models.py - TU NUEVO MODELO
from django.db import models

# 3 modelos con relaciones

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    detalle = models.TextField()

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="noticias")  # Relación con Autor
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="noticias")  # Relación con Categoria

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    # El método str sirve para que el admin muestre el título en lugar de “Noticia object”.

