from rest_framework import serializers
from .models import Evento, Ubicacion, Contacto


class EventoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Evento.
    """

    class Meta:
        model = Evento
        fields = '__all__'  # Serializa todos los campos del modelo


class UbicacionSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Ubicacion.
    """

    class Meta:
        model = Ubicacion
        fields = '__all__'  # Serializa todos los campos del modelo


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

    def update(self, instance, validated_data):
        fotografia = validated_data.get('fotografia', None)
        if fotografia is None and 'fotografia' in validated_data:
            validated_data.pop('fotografia')  # Elimina el campo si no se envía una nueva imagen
        return super().update(instance, validated_data)
