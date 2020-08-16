from django.urls import include, path, re_path
from rest_framework import routers

from music import model_viewsets as music_model_viewsets
from music import generic_views as music_generic_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'musican-viewset', music_model_viewsets.MusicianModelViewSet)


urlpatterns = [
    path(r'musican-views', music_generic_views.MusicListCreateView.as_view(), name='list_create_musican'),
    path(r'musican-views/<id>', music_generic_views.MusicRetrieveUpdateDestroyView.as_view(), name='get_musican'),
    path(r'musican-views/<id>/sample-action', music_generic_views.MusicRetrieveFullNameView.as_view(), name='get_musican_full_name'),
    re_path(r'^', include(router.urls))
]
