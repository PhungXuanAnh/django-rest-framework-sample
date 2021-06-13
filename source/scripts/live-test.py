# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import sys
import datetime

import django
from celery.schedules import crontab_parser

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


def test_crontab_parser():
    print('minutes: ', crontab_parser(60).parse('14,39'))
    print('minutes: ', crontab_parser(60).parse('*/15'))
    print('hours: ', crontab_parser(24).parse('*/4'))
    print('day_of_week: ', crontab_parser(7).parse('*'))
    print('day_of_month: ', crontab_parser(31, 1).parse('*/3'))
    print('months_of_year: ', crontab_parser(12, 1).parse('*/2'))
    print('months_of_year: ', crontab_parser(12, 1).parse('2-12/2'))

if __name__ == '__main__':
    # test_celery_sample_task()
    test_crontab_parser()
