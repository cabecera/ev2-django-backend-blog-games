"""
URL configuration for bloggames project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import redirect

from core import views as views_core
from comunidad import views as views_comunidad
from contacto import views as views_contacto
from galeria import views as views_galeria
from noticias import views as views_noticias

def redirect_gallery(request):
    return redirect('/galeria/', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_core.home,name="index"),
    # path('comunidad/',views_comunidad.comunidad,name="comunidad"),
    # path('contacto/',views_contacto.contacto,name="contacto"),
    path('galeria/', include('galeria.urls')),
    path('gallery/', redirect_gallery, name="redirect_gallery"),  # Redirección para /gallery/
    path('noticias/',views_noticias.noticias,name="noticias"),
]
