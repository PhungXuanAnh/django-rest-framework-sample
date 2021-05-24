from rest_framework import serializers
from coordinate.models import Coordinate


class CoordinateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ['latitude', 'longitude', 'created_at', 'battery_level']
