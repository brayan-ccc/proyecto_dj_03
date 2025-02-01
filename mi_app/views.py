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
        'fecha' : datetime.now(),
    }
    return render(request, 'mi_app/hola.html', contexto)

def saludo_herencia(request, nombre):
    return render(request,'mi_app/saludo.html', {'nombre':nombre}) 

def simple(request):
    return render(request,'mi_app/pagina_simple.html')

def mascota(request):
    datos_mascota = {
        "nombre" : "Firulais",
        "tipo" : "perro",
        "edad" : 5,
        "foto" : "🐶",
    }
    return render(request,'mi_app/mascota.html',{'datos_mascota':datos_mascota})

def lista_numeros(request):
    numeros = ["a",2,3,4,"b",6,7,8,9,10]
    return render(request,'mi_app/numeros.html',{'numeros':numeros})

def edad(request):
    usuario = {
        "nombre" : "Juancito",
        "profesion" : "programador",
        "edad" : 90,
    }
    return render(request,'mi_app/es_mayor.html', {'usuario':usuario})     
