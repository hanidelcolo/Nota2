from django.shortcuts import render
from post.models import News

def home(request):
    latest = list(News.objects.order_by('-created')[:3])
    stats = [
        (News.objects.count(), "reseñas publicadas"),
        (News.objects.filter(reading_status="leyendo").count(), "leyendo ahora"),
        (News.objects.filter(is_favorite=True).count(), "favoritos"),
    ]
    return render(request, "core/home.html", {
        'latest': latest,
        'featured': latest[0] if latest else None,
        'stats': stats,
    })