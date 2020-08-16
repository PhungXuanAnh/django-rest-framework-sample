from rest_framework import generics
from .models import Musician, Album

from .model_serializers import MusicianModelSerializer

class MusicListCreateView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer


class MusicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer
    lookup_field = "id"


class MusicRetrieveFullNameView(generics.RetrieveAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        firt_name = response.data["first_name"]
        last_name = response.data["last_name"]
        response.data = {"full_name": firt_name + " " + last_name}
        return response
