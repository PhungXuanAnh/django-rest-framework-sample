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


class MusicianModelSerializerReadEffective_SourceKeyword(serializers.ModelSerializer):
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


class MusicianModelSerializerReadEffective_SerializerMethod(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    instruments = serializers.SerializerMethodField()

    def get_instruments(self, obj):
        instruments = obj.instruments.all()
        if not instruments:
            return None
        return InstrumentsModelSerializerReadEffective(instruments, many=True).data

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_full_name(self, obj):
        return obj.get_full_name().upper()
    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            'full_name',
            'instruments'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.id == 1:
            representation['note'] = 'this is the first record'
        return representation

