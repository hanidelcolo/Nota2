from django.shortcuts import get_object_or_404, render
from .models import News


def post(request):
    news = News.objects.order_by('-created')
    return render(request, "core/post.html", {'news': news})


def post_detail(request, pk):
    item = get_object_or_404(News, pk=pk)
    newer = News.objects.filter(created__gt=item.created).order_by('created').first()
    older = News.objects.filter(created__lt=item.created).order_by('-created').first()
    return render(request, "core/post_detail.html", {
        'post': item,
        'newer': newer,
        'older': older,
    })
