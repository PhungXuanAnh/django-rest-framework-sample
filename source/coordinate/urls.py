from django.urls import include, re_path
from rest_framework import routers

from coordinate.views import CoordinateModelViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'coordinate', CoordinateModelViewSet, basename='coordinate')

urlpatterns = [
    re_path(r'^', include(router.urls))
]
