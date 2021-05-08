from django.urls import include, re_path
from rest_framework import routers

from screen.views import UnlockScreenUrlModelViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'unlock-screen-url', UnlockScreenUrlModelViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]
