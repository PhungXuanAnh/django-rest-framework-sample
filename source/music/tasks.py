import datetime
import logging

from celery import shared_task

"""
NOTE: 
The tasks you write will probably live in reusable apps, and reusable apps cannot depend 
on the project itself, so you also cannot import your app instance directly.
The @shared_task decorator lets you create tasks without having any concrete app instance
Reference:
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#using-the-shared-task-decorator
"""

logger = logging.getLogger("celery.task")


@shared_task
def sample_music_task(arg=None):
    # NOTE: write logging messages as below for avoid error pylint
    # Use lazy % formatting in logging functionspylint(logging-not-lazy)
    # reference: https://stackoverflow.com/a/29371584/7639845
    logger.error(
        "-------------------- > This is task from music app! %s at %s",
        arg,
        datetime.datetime.now(),
    )
    return arg
