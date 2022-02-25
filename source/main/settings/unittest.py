# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path(BASE_DIR).resolve().parent / "db.sqlite3",
    }
}
