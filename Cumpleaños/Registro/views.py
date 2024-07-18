from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'registro/registro.html', {'form': RegistroForm(), 'success_message': 'Formulario enviado con éxito'})  # Redirige con un mensaje de éxito
    else:
        form = RegistroForm()

    return render(request, 'registro/registro.html', {'form': form})
