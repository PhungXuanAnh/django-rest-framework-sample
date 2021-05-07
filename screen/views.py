import requests
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from screen.models import UnlockScreenUrl
from screen.serializers import UnlockScreenUrlModelSerializer


class UnlockScreenUrlModelViewSet(viewsets.ModelViewSet):
    queryset = UnlockScreenUrl.objects.all()
    serializer_class = UnlockScreenUrlModelSerializer

    @action(
        detail=True,
        methods=["get"],
        url_path="unlock",
    )
    def unlock(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            response = requests.get(instance.url)
            return Response(data={"result": response.text}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"result": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
