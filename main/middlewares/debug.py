import debugpy
import datetime
from . import debug_tmp

class DebugpyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        debugpy.listen(("0.0.0.0", 5678))
        # debugpy.listen(5678)
        debugpy.wait_for_client()
        debugpy.breakpoint()

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)   # pass request to next middleware or view if this is the last middleware

        # Code to be executed for each request/response after
        # the view is called.

        # NOTE: # change this file for reload server after a request debugged
        # import os
        # print("------------------- {}".format(os.getcwd()))
        with open("main/middlewares/debug_tmp.py", 'w+') as f:
            f.write('"' + str(datetime.datetime.now()) + '"')

        return response