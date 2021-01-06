import logging
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import filters, filterset
from rest_framework import viewsets, filters as rest_filters
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from music.models import Musician, Album
from music.serializers.model_serializers import MusicianModelSerializer



logger = logging.getLogger('django')

class CustomSearchFilter(rest_filters.SearchFilter):
    def get_search_fields(self, view, request):
        logger.info("Only search by last_name ================= {}".format(request.query_params))
        if request.query_params.get('last_name_only'):
            logger.info("Only search by last_name =================")
            return ['=last_name']
        return super(CustomSearchFilter, self).get_search_fields(view, request)


class MusicanFilter(filterset.FilterSet):
    min_num_stars = filters.NumberFilter(field_name="profile__num_stars", lookup_expr='gte')
    max_num_stars = filters.NumberFilter(field_name="profile__num_stars", lookup_expr='lte')

    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'min_num_stars', 'max_num_stars']


class MusicianModelViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    ## --- filter ---
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = MusicanFilter     # NOTE: using filterset_class cannot show filter field in swagger, only filterset_fields work
    # filterset_fields = ['first_name', 'last_name']  # --> this is shortcut of filterset_class, use it if not add more fields: min_num_stars, max_num_stars
    #                                                 # this more here: https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html#adding-a-filterset-with-filterset-class

    ## --- search_filter ---
    # filter_backends = [rest_filters.SearchFilter]
    filter_backends = [CustomSearchFilter]
    search_fields = ['=first_name', '=last_name', '=email', '=profile__city']

    ## --- ordering --- 
    # filter_backends = [rest_filters.OrderingFilter]
    # ordering_fields = ['username', 'email']

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

