from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def hola_mundo(request):
    return HttpResponse("<h2>Hola mundo desde DJANGO 5.1</h2>")

def es_par(request, numero):
    if numero % 2 == 0:
        return HttpResponse(f"El número {numero} es PAR")
    else:
        return HttpResponse(f"El número {numero} es IMPAR")       
    
def mostrar_datos(request, nombre, edad):
    return HttpResponse(f"Nombre: {nombre} Edad: {edad}")

def hola_plantilla(request, nombre):
    contexto = {
        'nombre' : nombre,
        'fecha' : datetime.now().strftime("%d/%m/%Y"),
    }
    return render(request, 'mi_app/hola.html', contexto)

def saludo_herencia(request, nombre):
    return render(request,'mi_app/saludo.html', {'nombre':nombre}) 