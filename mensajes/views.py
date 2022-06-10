from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pagina_principal_mensajes(request):
    return HttpResponse("<h1>Pagina principal de mensajes</h1>")
