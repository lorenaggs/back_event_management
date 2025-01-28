from rest_framework import viewsets
from .models import Evento, Ubicacion, Contacto
from .serializers import EventoSerializer, UbicacionSerializer, ContactoSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class UbicacionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de las ubicaciones.
    """
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer


class ContactoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de los contactos.
    """
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
