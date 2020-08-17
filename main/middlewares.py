import debugpy
from django.utils.deprecation import MiddlewareMixin

class DebugpyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # debugpy.listen(("0.0.0.0", 5678))
        
        debugpy.listen(5678)
        debugpy.wait_for_client()

        debugpy.breakpoint()
        return None

    def process_response(self, request, response):
        debugpy.breakpoint()
        return response

    def process_exception(self):
        pass
