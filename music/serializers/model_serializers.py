from rest_framework import serializers
from music.models import Musician, Instrument


class InstrumentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name']


class MusicianModelSerializer(serializers.ModelSerializer):
    instruments = InstrumentModelSerializer(read_only=True, many=True)
    class Meta:
        model = Musician
        fields = ['id', 'first_name', 'last_name', 'instruments']