# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import django
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from music.models import Album, Musician, Profile
from coordinate.models import Coordinate

for coo in Coordinate.objects.all().order_by('created_at'):
    print(coo.created_at)
