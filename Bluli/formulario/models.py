from django.db import models

class Formulario(models.Model):

    ROUTE_CHOICES = [
        ('carro', 'carro'),
        ('route2', 'Route 2'),
        ('route3', 'Route 3'),]

    name = models.CharField(max_length=200, default='default')
    tfn = models.CharField(max_length=15)
    image = models.ImageField(upload_to="Formulario", null=True, blank=True)
    ruta = models.CharField(max_length=20, choices=ROUTE_CHOICES, default='route1')

    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Updated Date")
    
    def __str__(self):
        return self.name