from django.db import models

# Create your models here.

class Registro (models.Model):

    name = models.CharField(max_length=100)
    tfn = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='Registro')
    asistentes = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Updated Date")
        
    def __str__(self):
        return self.name