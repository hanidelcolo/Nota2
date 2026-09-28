from django.shortcuts import render

def post(request):
    news=News.objects.all()
    return render(request,"post/post.html",{'news':news})
# Create your views here.
