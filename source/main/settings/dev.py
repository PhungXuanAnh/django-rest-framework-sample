# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=wrong-import-order

from .base import *

# ==================== debug tool bar =========================

# # re-define this variable for each environment
# ALLOWED_HOSTS = ["localhost"]   
# # allow host using https, re-define this variable for each environment
# CSRF_TRUSTED_ORIGINS = ["https://localhost"]

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda _: DEBUG,
}
