from rest_framework import serializers
from .models import Sve

class SerializerInstrumenata(serializers.ModelSerializer):
    class Meta:
        model = Sve
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)