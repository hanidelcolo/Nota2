from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class News(models.Model):
    PALETTE_CHOICES = [
        ("rosa", "Rosa"),
        ("lila", "Lila"),
        ("beige", "Beige"),
    ]
    READING_STATUS_CHOICES = [
        ("leido", "Leído"),
        ("leyendo", "Leyendo"),
        ("pendiente", "Pendiente"),
    ]

    title = models.CharField(max_length=100, verbose_name="Titulo")
    author = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Autor",
        help_text="Ej: Hongduck · Nemone",
    )
    category = models.CharField(
        max_length=60,
        blank=True,
        verbose_name="Categoría",
        help_text="Ej: Romance · Slice of life",
    )
    reading_status = models.CharField(
        max_length=10,
        choices=READING_STATUS_CHOICES,
        default="leido",
        verbose_name="Estado de lectura",
    )
    is_favorite = models.BooleanField(default=False, verbose_name="Favorito")
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.5,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Puntuación",
        help_text="De 0 a 5, con un decimal. Ej: 4.8",
    )
    blurb = models.CharField(
        max_length=160,
        blank=True,
        verbose_name="Resumen corto",
        help_text="Una o dos frases para las tarjetas. Si lo dejas vacío se usa el inicio del detalle.",
    )
    detail = models.TextField(verbose_name="Detalle")
    palette = models.CharField(
        max_length=10,
        choices=PALETTE_CHOICES,
        default="rosa",
        verbose_name="Color de la portada",
    )
    image = models.ImageField(
        upload_to="news",
        blank=True,
        verbose_name="Imagen",
        help_text="Opcional. Si la subes, reemplaza la portada de colores.",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="F.de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="F. de Edición")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.title

    @property
    def summary(self):
        """Texto corto para tarjetas y listados."""
        if self.blurb:
            return self.blurb
        text = self.detail.strip()
        return text if len(text) <= 120 else text[:117].rstrip() + "…"
