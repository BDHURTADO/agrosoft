from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('cultivos/', include('cultivos.urls')),
    path('comercio/', include('comercio.urls')),
    path('sensores/', include('sensores.urls')),
    path('mapas/', include('mapas.urls')),
    path('reportes/', include('reportes.urls')),
]
