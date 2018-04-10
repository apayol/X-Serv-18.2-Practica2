from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Urls
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

FORMULARIO = """
    <form action="" method="POST">
        Introduzca URL para reducir:
        <input type="text" name="url_larga" value="http://">
        <input type="submit" value="Enviar">
    </form>
"""

def estandar_url(url_larga):
    if url_larga.startswith("http://") or url_larga.startswith("https://"):
        return url_larga
    else:
        return ("http://" + url_larga)

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
        url_larga = request.POST["url_larga"]
        url_larga = estandar_url(url_larga)
        try:  # busco si ya está guardada
            busco = Urls.objects.get(url_larga=url_larga)
            respuesta = "Esa url ya fue acortada y está guardada" 
        except Urls.DoesNotExist:  # no está guardada
            nueva = Urls(url_larga=url_larga)
            nueva.save()
            respuesta = "Ha sido guardada" 
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

def inco_entrada(request):
    respuesta = "Recurso incorrecto. Debe introducir <big><b>localhost:8000/[num]</b></big>"
    return HttpResponse(respuesta)


