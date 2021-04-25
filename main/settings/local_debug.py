from .local import *

MIDDLEWARE.insert(0, 'main.middlewares.debug.DebugpyMiddleware')
