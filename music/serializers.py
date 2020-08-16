from rest_framework import serializers


class MusicianSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    instrument = serializers.CharField(max_length=100)