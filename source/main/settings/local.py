# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=wrong-import-order

from .dev import *

# # re-define this variable for each environment
# ALLOWED_HOSTS = ["localhost"]   
# # allow host using https, re-define this variable for each environment
# CSRF_TRUSTED_ORIGINS = ["https://localhost"]

# ============================= disable sentry ================================================
import sentry_sdk

# NOTE: call sentry init again with empty arguments for disable sentry
# reference: https://github.com/getsentry/sentry-python/issues/660#issuecomment-604077472
sentry_sdk.init()
