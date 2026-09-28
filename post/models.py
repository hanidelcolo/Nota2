from django.db import models

class News(models.Model):
    title=models.CharField(max_length=100,verbose_name="Titulo")
    detail=models.TextField(verbose_name="Detalle")
    image=models.ImageField()
    created=models.DateTimeField(auto_now=True,auto_now_add=True,verbose_name="F. de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="F. de edición")

    class Meta:
        verbose_name="Noticia"
        verbose_name_plural="Noticias"

    def __str__(self):
        return self.title

# Create your models here.
