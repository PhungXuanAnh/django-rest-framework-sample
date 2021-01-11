from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from coordinate.models import Coordinate
from coordinate.serializers import CoordinateModelSerializer

class CoordinateModelViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateModelSerializer
    # permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['created_at']
    ordering = ['created_at']