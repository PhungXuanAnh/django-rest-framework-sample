import pytz
from rest_framework import serializers
from coordinate.models import Coordinate


class CoordinateModelSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Coordinate
        fields = ["latitude", "longitude", "created_at", "battery_level"]

    def get_created_at(self, obj):
        return obj.created_at.astimezone(pytz.timezone("Asia/Ho_Chi_Minh")).strftime(
            "[%Y-%m-%d]-[%H:%M:%S]"
        )
