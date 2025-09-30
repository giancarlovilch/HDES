from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views  # o mejor usar core.views si lo mueves

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  

    # Apps principales
    path('schedule/', include('schedule.urls', namespace='schedule')),  
    path('inventory/', include('inventory.urls', namespace='inventory')),
    path('sales/', include('sales.urls', namespace='sales')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('suppliers/', include('suppliers.urls', namespace='suppliers')),
    path('accounts/', include('accounts.urls', namespace='accounts')),  
    path('legal/', include('legal.urls', namespace='legal')),  
    path('api/', include('api.urls', namespace='api')),

    # Autenticación
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
