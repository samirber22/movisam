from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from controlador import views
from django.conf import settings
from django.conf.urls.static import static
import os
from django.contrib.auth.views import LogoutView
from usuarios.forms import LoginFormPersonalizado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='inicio'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        authentication_form=LoginFormPersonalizado
    ), name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('register/', views.register, name='register'),
    path('rutas/', views.rutas, name='rutas'),
    path('horarios/', views.horarios, name='horarios'),
    path('admin-rutas/', views.admin_rutas, name='admin_rutas'),
    path('eliminar-ruta/<int:ruta_id>/', views.eliminar_ruta, name='eliminar_ruta'),
]

urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'public'))