from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.hola_mundo),
    path('es_par/<int:numero>',views.es_par),
    path('datos/<str:nombre>/<int:edad>', views.mostrar_datos),
    path('hola_plantilla/<str:nombre>',views.hola_plantilla),
    path('saludo_herencia/<str:nombre>', views.saludo_herencia),
]
