from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def saludo(request):
    return HttpResponse("Hola a todos")


def renderTemplate(request):
    data = {"nombre":"Fabian"}
    return render(request, 'templateAPP1/plantilla.html', data)