from main.paginations.custom_paginations import CustomPagination
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework import filters as rest_filters
from rest_framework.decorators import action
from rest_framework.response import Response


from coordinate.models import Coordinate
from coordinate.serializers import CoordinateModelSerializer

class CoordinateModelViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateModelSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # ordering
    filter_backends = [rest_filters.OrderingFilter]
    ordering_fields = ['created_at']
    ordering = ['created_at']

    # pagination
    pagination_class = CustomPagination