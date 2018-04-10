from django.shortcuts import render
from django.http import HttpResponse
from .models import Urls

# Create your views here.

FORMULARIO = """
    <form action="" method="POST">
        Introduzca URL para reducir:
        <input type="text" name="URL" value="http://">
        <input type="submit" value="Enviar">
    </form>
"""

def bienvenida(request):
    if request.method == "GET":
        respuesta = "<h3>Bienvenido a acortadorURLs</h3>"
        respuesta += "<br>URLs guardadas:"
        urls = Urls.objects.all()
        for url in urls:
            respuesta += "<br>Url original: " + url.name + " => Url corta: " + str(url.id)
        respuesta += "<br><br>" + FORMULARIO

    return HttpResponse(respuesta)

def redir(request, url_corta):
    return HttpResponse("<h3>Redirección</h3>")
