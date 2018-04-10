from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Urls
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

FORMULARIO = """
    <form action="" method="POST">
        Introduzca URL para reducir:
        <input type="text" name="URL" value="http://">
        <input type="submit" value="Enviar">
    </form>
"""

@csrf_exempt
def bienvenida(request):
    if request.method == "GET":
        respuesta = "<h3>Bienvenido a acortadorURLs</h3>"
        respuesta += "<br><b>URLs guardadas:</b>"
        urls = Urls.objects.all()
        for url in urls:
            respuesta += "<br>Url original: <a href=" + url.url_larga + ">" + url.url_larga + "</a>"
            respuesta += " => Url corta : <a href=" + str(url.id) + ">" + str(url.id) + "</a>"
        respuesta += "<br><br>" + FORMULARIO

    elif request.method == "POST":
        respuesta = "Es un post"
    else:
        respuesta = "Método no permitido"
    return HttpResponse(respuesta)

def redir(request, url_corta):
    if request.method == "GET":
        try: 
            url_larga = Urls.objects.get(id=url_corta).url_larga
            respuesta = url_larga
            return HttpResponseRedirect(respuesta)
        except Urls.DoesNotExist:
            respuesta = "Esa url no ha sido añadida aún"
    else:
        respuesta = "Método no permitido"
    return HttpResponse(respuesta)



