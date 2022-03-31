from django.conf import settings
from rest_framework.authentication import BasicAuthentication


class CustomAuthBackend(BasicAuthentication):
    def authenticate(self, request):
        if settings.DEBUG:
            import debugpy
            debugpy.breakpoint()
        return super().authenticate(request)
