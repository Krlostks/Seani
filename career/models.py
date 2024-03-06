from django.db import models

class Career(models.Model):

    LEVELS= [
        ('ing', 'Ingenieria'),
        ('TSU', 'Tecnico Superior Universitario'),
        ('M', 'Mestria')
    ]

    name = models.CharField( max_length=200 , verbose_name='Nombre')
    shortname = models.CharField(
        max_length=20,
        verbose_name='Abreviatura')
    level = models.CharField(
        max_length=10, 
        choices = LEVELS,
        verbose_name='Nivel')
    
    def __str__(self):
        return f"{ self.level } - { self.shortname }"

    class Meta:
        verbose_name='carrera'
        verbose_name_plural='carreras'