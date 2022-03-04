# pylint: disable=protected-access
# pylint: disable=broad-except
import datetime
import os
import sys

import django
import pytz
from celery.schedules import crontab_parser

sys.path.append(os.path.dirname(__file__) + "/../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.local")
django.setup()


from coordinate.models import Coordinate
from coordinate.tasks import check_battery_level

# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from main.celery_app import sample_task
from music.models import Album, Musician, Profile
from music.tasks import sample_music_task


def test_coordinate_app():
    # for coo in Coordinate.objects.all().order_by("created_at"):
    #     print(coo.created_at)
    #     print(coo.battery_level)

    # latest_coordinate = Coordinate.objects.all().order_by("-created_at").first()
    # print(latest_coordinate.created_at)
    # print(latest_coordinate.battery_level)

    # latest_coordinate = Coordinate.objects.all().order_by("-created_at").first()
    # print((datetime.datetime.now().astimezone() - latest_coordinate.created_at).seconds)
    # print(latest_coordinate.created_at.strftime("[%Y-%m-%d]-[%H:%M:%S]"))
    # print(latest_coordinate.created_at.astimezone(pytz.timezone("Asia/Ho_Chi_Minh")).strftime("[%Y-%m-%d]-[%H:%M:%S]"))
    pass


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


def test_crontab_parser():
    print("minutes: ", crontab_parser(60).parse("14,39"))
    print("minutes: ", crontab_parser(60).parse("*/15"))
    print("hours: ", crontab_parser(24).parse("*/4"))
    print("day_of_week: ", crontab_parser(7).parse("*"))
    print("day_of_month: ", crontab_parser(31, 1).parse("*/3"))
    print("months_of_year: ", crontab_parser(12, 1).parse("*/2"))
    print("months_of_year: ", crontab_parser(12, 1).parse("2-12/2"))


if __name__ == "__main__":
    # test_celery_sample_task()
    # test_coordinate_app()
    # test_celery_sample_task()
    test_crontab_parser()
