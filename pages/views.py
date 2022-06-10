from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina_principal_pages(request):
    return render(request,"pages/pages.html")


