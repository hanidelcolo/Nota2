from django.shortcuts import render
from .models import News

def post(request):
    news=News.objects.all()
    return render(request,"core/post.html",{'news':news})
# Create your views here.
