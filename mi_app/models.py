from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre} Fecha: {self.fecha_inicio}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) # Relacionando Estudiantes a un curso (Muchos a 1)
    
    def __str__(self):
        return self.nombre
    
    