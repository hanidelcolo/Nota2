from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Recibido")

    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"
        ordering = ['-created']

    def __str__(self):
        return f"{self.name} <{self.email}>"

# Create your models here.
