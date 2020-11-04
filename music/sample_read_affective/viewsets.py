from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from music.models import Musician, Album
from music.sample_read_affective.serializers import MusicianModelSerializerReadEffective


class MusicianModelReadEffectiveViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializerReadEffective
    # permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=True,
        methods=["get"],
        url_path="sample-action",  # if not specify, it will using name of method
        permission_classes=[permissions.IsAuthenticated],
    )
    def get_full_name(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(
            data={"full_name": instance.first_name + " " + instance.last_name}, status=status.HTTP_200_OK
        )

