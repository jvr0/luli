from django.shortcuts import render, redirect
from .forms import FormularioForm

def formulario_view(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    else:
        form = FormularioForm()
        
    return render(request, 'formulario_template.html', {'form': form})