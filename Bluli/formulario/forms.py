from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    tfn = forms.CharField(max_length=15)
    image = forms.ImageField(upload_to="Formulario", null=True, blank=True)


    class Meta:
        model = Formulario
        fields = ['name', 'tfn', 'image', 'ruta']