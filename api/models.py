from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
import os
from uuid import uuid4

from backend.settings import BASE_DIR

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    invitados = models.TextField()
    fecha_hora = models.DateTimeField()
    zona_horaria = models.CharField(
        max_length=50,
        choices=[('UTC-5', 'UTC-5'), ('UTC+0', 'UTC+0'), ('UTC+5', 'UTC+5')],
        default='UTC+0'
    )
    descripcion = models.TextField(blank=True, null=True)
    repeticion = models.CharField(
        max_length=50,
        choices=[('Ninguna', 'Ninguna'), ('Diaria', 'Diaria'), ('Semanal', 'Semanal')],
        default='Ninguna'
    )
    recordatorio = models.BooleanField(default=False)
    clasificacion = models.CharField(max_length=100, blank=True, null=True)
    lugar = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Ubicacion(models.Model):
    titulo = models.CharField(max_length=255)
    direccion = models.TextField()
    coordenadas = models.CharField(max_length=50, blank=True, null=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)  # Agregar default=0.0
    longitud = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)  # Agregar default=0.0

    def __str__(self):
        return self.titulo


def custom_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.nombre_completo}_{uuid4().hex}.{ext}"
    return os.path.join('fotografias/', filename)



class Contacto(models.Model):
    saludo = models.CharField(
        max_length=20,
        choices=[('Sr.', 'Sr.'), ('Sra.', 'Sra.'), ('Dr.', 'Dr.')],
        default='Sr.'
    )
    nombre_completo = models.CharField(max_length=255)
    numero_identificacion = models.CharField(max_length=50, unique=True)
    correo_electronico = models.EmailField(unique=True)
    numero_telefono = models.CharField(max_length=15)
    fotografia = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)

    def __str__(self):
        return self.nombre_completo
