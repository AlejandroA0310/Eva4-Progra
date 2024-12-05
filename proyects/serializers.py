from rest_framework import serializers
from .models import Proyect

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'title', 'description', 'estado_alumno', 'technology', 'created_at')
        read_only_fields = ('created_at',)

    def update(self, instance, validated_data):
        # Actualizar solo el campo 'estado_alumno' si es proporcionado
        instance.estado_alumno = validated_data.get('estado_alumno', instance.estado_alumno)
        instance.save()
        return instance
