import debugpy
from rest_framework.authentication import BasicAuthentication

class CustomAuthBackend(BasicAuthentication):
    def authenticate(self, request):
        debugpy.breakpoint()
        return super().authenticate(request)
