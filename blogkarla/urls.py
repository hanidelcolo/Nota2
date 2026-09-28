"""
URL configuration for blogkarla project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from about import views as about_views
from contact import views as contact_views
from post import views as post_views

urlpatterns = [
    path('',core_views.home,name="home"),
    path('about/',about_views.about,name="about"),
    path('contact/',contact_views.contact,name="contact"),
    path('post/',post_views.post,name="post"),
    path('admin/', admin.site.urls),
]
