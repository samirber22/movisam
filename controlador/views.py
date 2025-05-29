from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from usuarios.forms import RegistroFormPersonalizado
from modelo.models import Ruta
from django.http import JsonResponse

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
    rutas = Ruta.objects.filter(activa=True)
    return render(request, 'rutas.html', {'rutas': rutas})

def horarios(request):
    return render(request, 'horario.html')

@user_passes_test(lambda u: u.es_admin)
def admin_rutas(request):
    if request.method == 'POST':
        # Crear o actualizar ruta
        ruta_id = request.POST.get('ruta_id')
        if ruta_id:
            ruta = get_object_or_404(Ruta, id=ruta_id)
        else:
            ruta = Ruta()
        
        ruta.nombre = request.POST.get('nombre')
        ruta.descripcion = request.POST.get('descripcion')
        ruta.origen = request.POST.get('origen')
        ruta.destino = request.POST.get('destino')
        ruta.paradas = request.POST.get('paradas')
        ruta.save()
        
        return redirect('admin_rutas')
    
    rutas = Ruta.objects.all()
    return render(request, 'admin_rutas.html', {'rutas': rutas})

@user_passes_test(lambda u: u.es_admin)
def eliminar_ruta(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    ruta.activa = False
    ruta.save()
    return JsonResponse({'status': 'success'})