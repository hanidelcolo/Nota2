from django.shortcuts import render
from .models import News


def post(request):
    news = News.objects.order_by('-created')
    return render(request, "core/post.html", {'news': news})

# Create your views here.
