from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

#El método __str__ sirve para que el admin muestre el título en lugar de “Noticia object”.
    def __str__(self):
        return self.titulo