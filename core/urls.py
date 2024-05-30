"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from article.views import (
    home__view, 
    about__view, 
    contact__view, 
    my__blogs__view, 
    our__blogs__view
)
urlpatterns = [
    path("", home__view, name="home"),
    path("about/", about__view, name="about"),
    path("contact/", contact__view, name="contact"),
    path("blogs/", our__blogs__view, name="our-blogs"),
    path("my-blogs/", my__blogs__view, name="my-blogs"),
    path("account/", include("account.urls")),
    path('admin/', admin.site.urls),
]
