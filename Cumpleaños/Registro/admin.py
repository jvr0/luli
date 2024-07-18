from django.contrib import admin
from .models import Registro

class RegistroAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Registro, RegistroAdmin)