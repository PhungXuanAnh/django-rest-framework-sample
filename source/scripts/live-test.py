# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import sys
import datetime

import django
import datetime

sys.path.append(os.path.dirname(__file__) + "/../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.local")
django.setup()


# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from main.celery_app import sample_task
from music.models import Album, Musician, Profile
from coordinate.models import Coordinate
from coordinate.tasks import check_battery_level
from music.tasks import sample_music_task


def test_coordinate_app():
    for coo in Coordinate.objects.all().order_by("created_at"):
        print(coo.created_at)
        print(coo.battery_level)

    latest_coordinate = Coordinate.objects.all().order_by("-created_at").first()
    print(latest_coordinate.created_at)
    print(latest_coordinate.battery_level)


def test_music_app():
    musican = Musician.objects.get(id=1)
    print(musican.album_set.all())


def test_celery_sample_task():
    # sample_task.apply_async(queue="queue-low")
    # sample_music_task.apply_async(queue="queue-high")
    # sample_task.apply_async()
    # sample_music_task.apply_async()
    # check_battery_level.apply_async(queue="queue-high")
    check_battery_level()


if __name__ == "__main__":
    test_celery_sample_task()
    # test_coordinate_app()

    latest_coordinate = Coordinate.objects.all().order_by("-created_at").first()
    print((datetime.datetime.now().astimezone() - latest_coordinate.created_at).seconds)
