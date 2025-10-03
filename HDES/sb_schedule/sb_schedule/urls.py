from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views   # index, php_login_form, php_logout

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home / Dashboard
    path('', views.index, name='index'),

    # Auth vía PHP
    path('login/', views.php_login_form, name='php_login_form'),
    path('logout/', views.php_logout, name='php_logout'),

    # Apps
    path('schedule/', include('schedule.urls', namespace='schedule')),
    path('inventory/', include('inventory.urls', namespace='inventory')),
    path('sales/', include('sales.urls', namespace='sales')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('suppliers/', include('suppliers.urls', namespace='suppliers')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('legal/', include('legal.urls', namespace='legal')),

    # API
    path('api/', include('api.urls', namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
