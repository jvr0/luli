from django.contrib import admin
from .models import Formulario

# Register your models here.

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('name', 'tfn', 'image', 'ruta', 'created', 'updated')
    list_filter = ('ruta', 'created')
    search_fields = ('name', 'tfn')