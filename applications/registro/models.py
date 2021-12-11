from django.db import models

from applications import registro

#Creo los modelos

#Creo el modelo Docente
class Docente(models.Model):

    #Para elegir la materia de cada Docente
    MATERIA = (
        ('0', 'Programación 2'),
        ('1', 'Práctica 1'),
        ('2', 'Matemática Aplicada'),
        ('3', 'Modelado de Sistemas'),
        ('4', 'Sistemas Operativos'),
        ('5', 'Base de Datos'),
    )

    #Defino los atributos de Docente
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=150, blank=True)
    age = models.CharField('Edad', max_length=50)
    avatar = models.ImageField('Imagen', upload_to='registro', height_field=None, width_field=None, max_length=None, blank=True)
    materia = models.CharField('Materia', max_length=50, choices=MATERIA)

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        return self.last_name + ', ' + self.first_name

#Creo el modelo No Docente
class NoDocente(models.Model):

    #Para elegir la oficina a la cuál pertenece
    AREA = (
        ('0', 'Limpieza'),
        ('1', 'Administrativo'),
        ('2', 'Tesorería'),
        ('3', 'Dirección'),
    )

    #Defino los atributos de No Docente
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=150, blank=True)
    age = models.CharField('Edad', max_length=50)
    oficina = models.CharField('Área', max_length=50, choices=AREA)
    avatar = models.ImageField('Imagen', upload_to='registro', height_field=None, width_field=None, max_length=None, blank=True)

    class Meta:
        verbose_name = 'No Docente'
        verbose_name_plural = 'No Docentes'

    def __str__(self):
        return self.last_name + ', ' + self.first_name