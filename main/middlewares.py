import debugpy
from django.utils.deprecation import MiddlewareMixin

# class DebugpyMiddleware(MiddlewareMixin):

#     def process_request(self, request):
#         # debugpy.listen(("0.0.0.0", 5678))
        
#         debugpy.listen(5678)
#         debugpy.wait_for_client()

#         debugpy.breakpoint()
#         return None

#     def process_response(self, request, response):
#         debugpy.breakpoint()
#         return response

#     def process_exception(self):
#         pass


class DebugpyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # debugpy.listen(("0.0.0.0", 5678))
        debugpy.listen(5678)
        debugpy.wait_for_client()
        debugpy.breakpoint()

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)   # pass request to next middleware or view if this is the last middleware

        # Code to be executed for each request/response after
        # the view is called.

        return response