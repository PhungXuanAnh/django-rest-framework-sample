from rest_framework import serializers
from screen.models import UnlockScreenUrl


class UnlockScreenUrlModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnlockScreenUrl
        fields = ['url']
