from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, UbicacionViewSet, ContactoViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'ubicaciones', UbicacionViewSet)
router.register(r'contactos', ContactoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:  # Solo en modo DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
