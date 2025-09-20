# sb_schedule/urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Asegúrate de que 'views' existe en este directorio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Página principal (ya existente)
    path('schedule/', include('schedule.urls', namespace='schedule')),  # Ya existente
    
    # NUEVOS MÓDULOS - Crea apps separadas para estos y agrega 'urls.py' en cada app
    path('inventory/', include('inventory.urls', namespace='inventory')),
    path('sales/', include('sales.urls', namespace='sales')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('suppliers/', include('suppliers.urls', namespace='suppliers')),
    path('accounts/', include('accounts.urls', namespace='accounts')),  # Para perfil/logout
    path('legal/', include('legal.urls', namespace='legal')),  # Para privacidad/términos
    
    # Placeholder para rutas que no tengan app aún (evita errores ; usa vistas temporales)
    # path('inventory/', views.placeholder_inventory, name='inventory:placeholder'),  # Ejemplo temporal
]

# Configurar rutas para logout básico si usas Django auth (agrega si no está)
from django.contrib.auth import views as auth_views
urlpatterns += [
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Página de redirección después de logout
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)