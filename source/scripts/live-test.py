# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import sys
import django

sys.path.append(os.path.dirname(__file__) + '/../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.local")
django.setup()

# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from music.models import Album, Musician, Profile
import datetime

musican = Musician.objects.get(id=1)
print(musican.album_set.all())
