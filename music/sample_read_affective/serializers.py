from rest_framework import serializers
from music.models import Musician, Album, Instrument


class AlbumModelSerializerReadEffective(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class InstrumentsModelSerializerReadEffective(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name']


class MusicianModelSerializerReadEffective(serializers.ModelSerializer):
    new_first_name = serializers.CharField(source="first_name")
    full_name = serializers.CharField(source="get_full_name")
    street = serializers.CharField(source="profile.street")
    city = serializers.CharField(source="profile.city")
    full_address = serializers.CharField(source="profile.get_full_address")
    all_albums = AlbumModelSerializerReadEffective(source='album_set', many=True)
    instruments = InstrumentsModelSerializerReadEffective(many=True)

    class Meta:
        model = Musician
        fields = [
            "id",
            "new_first_name",
            "last_name",
            "full_name",
            "street",
            "city",
            "full_address",
            'all_albums',
            'instruments'
        ]

