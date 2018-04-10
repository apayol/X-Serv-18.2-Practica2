from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bienvenida(request):
    return HttpResponse("<h3>Bienvenido a acortadorURLs<h3>")

def redir(request, url_corta):
    return HttpResponse("<h3>Redirección<h3>")
