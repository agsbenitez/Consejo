"""
Este archivo fue creado manualemte a mode de poder correr los primeros ejemplo de views
"""

from django.http import HttpResponse
from datetime import datetime


def saludo(request):
    return HttpResponse("Primer Vista con Django")


def hoy(request):
    _hoy= datetime.now()
    return HttpResponse(f'hoy es: {_hoy} ')


def saludar_a(request, nombre):
    return HttpResponse (f'Hola { nombre}')


def cuando_naci(request, edad):
    return HttpResponse(f'Naciste el {(datetime.now().year - int(edad)) }')