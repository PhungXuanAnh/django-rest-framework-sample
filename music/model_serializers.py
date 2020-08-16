from rest_framework import serializers
from .models import Musician

class MusicianModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['id', 'first_name', 'last_name', 'instrument']