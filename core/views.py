from django.shortcuts import render
from post.models import News


def home(request):
    latest = list(News.objects.order_by('-created')[:3])
    reading_now = list(
        News.objects.filter(reading_status="leyendo").order_by('-updated', '-created')
    )
    stats = [
        (News.objects.count(), "reseñas publicadas"),
        (News.objects.filter(reading_status="leyendo").count(), "leyendo ahora"),
        (News.objects.filter(is_favorite=True).count(), "favoritos"),
    ]
    return render(request, "core/home.html", {
        'latest': latest,
        'reading_now': reading_now,
        'featured': reading_now[0] if reading_now else None,
        'stats': stats,
    })
