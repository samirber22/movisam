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

def buscar_ruta(request):
    if request.method == 'POST':
        origen = request.POST.get('origen', '').lower()
        destino = request.POST.get('destino', '').lower()
        
        # Buscar rutas que coincidan con el origen y destino
        rutas = Ruta.objects.filter(
            activa=True,
            origen__icontains=origen,
            destino__icontains=destino
        )
        
        if rutas.exists():
            rutas_data = [{
                'nombre': ruta.nombre,
                'descripcion': ruta.descripcion,
                'origen': ruta.origen,
                'destino': ruta.destino,
                'paradas': ruta.paradas.split('\n')
            } for ruta in rutas]
            return JsonResponse({'found': True, 'rutas': rutas_data})
        else:
            return JsonResponse({'found': False, 'message': 'No se encontraron rutas para este trayecto.'})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@user_passes_test(lambda u: u.es_admin)
def admin_rutas(request):
    if request.method == 'POST':
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