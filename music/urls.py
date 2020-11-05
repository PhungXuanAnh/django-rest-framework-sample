from django.urls import include, path, re_path
from rest_framework import routers

from music import model_viewsets as music_model_viewsets
from music import generic_views as music_generic_views
from music import api_views as music_api_views
from music import debug_views as music_debug_views
from music.sample_read_affective import viewsets as read_affective

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'musican-viewset', music_model_viewsets.MusicianModelViewSet)
router.register(r'musican-debug', music_debug_views.MusicianModelDebugViewSet)
router.register(r'musican-read-affective-source-keyword', read_affective.MusicianModelReadEffective_SourceKeyword_ViewSet)
router.register(r'musican-read-affective-serializer-method', read_affective.MusicianModelReadEffective_SerializerMethod_ViewSet)

urlpatterns = [
    path(r'musican-api-views', music_api_views.CreateListMusicanView.as_view(), name='api_view_list_musican'),
    path(r'musican-api-views/<id>', music_api_views.MusicanRetriveUpdateDestroyView.as_view(), name='api_view_getputpatchdelete_musican'),
    path(r'musican-api-views/<id>/sample-action', music_api_views.MusicanFullNameView.as_view(), name='api_view_full_name_musican'),

    path(r'musican-generic-views', music_generic_views.MusicListCreateView.as_view(), name='list_create_musican'),
    path(r'musican-generic-views/<id>', music_generic_views.MusicRetrieveUpdateDestroyView.as_view(), name='get_musican'),
    path(r'musican-generic-views/<id>/sample-action', music_generic_views.MusicRetrieveFullNameView.as_view(), name='get_musican_full_name'),
    
    re_path(r'^', include(router.urls))
]
