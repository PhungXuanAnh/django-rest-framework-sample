# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import sys
import datetime

import django

sys.path.append(os.path.dirname(__file__) + '/../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.local")
django.setup()


# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from main.celery_app import sample_task
from music.models import Album, Musician, Profile
from music.tasks import sample_music_task


def test_music_app():
    musican = Musician.objects.get(id=1)
    print(musican.album_set.all())

def test_celery_sample_task():
    # sample_task.apply_async(queue="queue-low")
    # sample_music_task.apply_async(queue="queue-high")
    sample_task.apply_async()
    sample_music_task.apply_async()


if __name__ == '__main__':
    test_celery_sample_task()
