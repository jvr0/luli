from django.db import models

# Create your models here.

class Registro (models.Model):

    Nombre = models.CharField(max_length=100)
    Teléfono = models.CharField(max_length=15)
    Edad = models.IntegerField()
    Imágen = models.ImageField(upload_to='Registro', verbose_name='Subí tu foto preferida conmigo para el mural')
    Notas = models.CharField(max_length=100)



    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Updated Date")
        
    def __str__(self):
        return self.Nombre