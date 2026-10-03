from django.shortcuts import render

def about(request):
    return render(request,"core/about.html")

# Create your views here.
