from usuarios.forms import RegistroFormPersonalizado
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistroFormPersonalizado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroFormPersonalizado()
    return render(request, 'register.html', {'form': form})

def rutas(request):
    return render(request, 'rutas.html')

def horarios(request):
    return render(request, 'horario.html')