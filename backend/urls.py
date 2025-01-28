from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Rutas de tu API
    path('', lambda request: HttpResponseRedirect('/api/')),  # Redirige la raíz a /api/
]

if settings.DEBUG:  # Solo en modo DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
