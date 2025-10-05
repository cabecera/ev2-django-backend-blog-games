from django.db import models

# Create your models here.
class Comunidad(models.Model):
    titulo = models.CharField(max_length=100)
    detalle = models.TextField()
    autor = models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="projects",
                            verbose_name="Imagen")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
# El método str sirve para que el admin muestre el título en lugar de “Noticia object”.



    class Meta:
        verbose_name = "Comunidad"
        verbose_name_plural = "Comunidad"
