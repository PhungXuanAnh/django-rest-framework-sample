from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Musician, Album
from .model_serializers import MusicianModelSerializer


class MusicianModelViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=True,
        methods=["get"],
        url_path="example-action",  # if not specify, it will using name of method
        permission_classes=[permissions.IsAuthenticated],
    )
    def example_action(self, request, *args, **kwargs):
        return Response(
            data={"message": "This is example action"}, status=status.HTTP_200_OK
        )

