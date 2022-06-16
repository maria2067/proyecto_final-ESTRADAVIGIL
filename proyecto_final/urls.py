"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


def pagina_principal(request):
    return render(request , 'index.html') # forma de importar archivo html


def pagina_about(request):
    return render(request , 'about.html') # forma de importar archivo html


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal, name="pagina principal"),
    path('about/' ,pagina_about,name="about"),


    path('accounts/' , include('accounts.urls')),
    path('mensajes/' , include('mensajes.urls')),
    path('pages/' , include('pages.urls')),
    path('contact/', include('contact.urls')),
    path('feedback/', include('feedback.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# add a flag for
# handling the 404 error
#handler404 = 'pages.views.error_404_view'
