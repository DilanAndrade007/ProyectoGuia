from django.db import models
from ProyectoGuia.Apps.facultad.models import Facultad
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural = 'Habilidades de los estudiantes'

    def __str__(self):
        return self.habilidad


class Estudiante(models.Model):
    tiposEstudiantes = (
        ('0', 'Nivelación'),
        ('1', 'Pregrado'),
        ('2', 'Maestría'),
        ('3', 'Doctorado')
    )
    primerNombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellidos', max_length=50)
    nombreCompleto = models.CharField('Nombre Completo', max_length=100, blank=True)
    tipo = models.CharField('Tipo', max_length=1, choices=tiposEstudiantes)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    # imagen
    # Carta motivación
    cartaMotivacion = RichTextField()
    # Relación muchos a muchos
    habilidad = models.ManyToManyField(Habilidades)

    class Meta:
        #nombre singular
        verbose_name='Estudiante'
        #nombre plural
        verbose_name_plural = 'Estudiantes matriculados'
        ordering = ['id']

    def __str__(self):
        return self.primerNombre + ' '+ self.apellido + ' - Facultad: ' +self.facultad.nombreCorto

