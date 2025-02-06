from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()

    def __str__(self):
        #return f"Nombre: {self.nombre} Fecha: {self.fecha_inicio}"
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, null = True, blank = True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes') # Relacionando Estudiantes a un curso (Muchos a 1)
    
    def __str__(self):
        return self.nombre
    
    