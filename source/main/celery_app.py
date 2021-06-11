import os

from celery import Celery
from celery.signals import setup_logging

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.local")

app = Celery("MY-CELERY-APP")
app.config_from_object("main.settings.celeryconfig")
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task
def sample_task(*arg, **kwargs):
    # pylint: disable=import-outside-toplevel
    import datetime
    import logging

    # NOTE: write logging messages as below for avoid error pylint
    # Use lazy % formatting in logging functionspylint(logging-not-lazy)
    # reference: https://stackoverflow.com/a/29371584/7639845
    logger = logging.getLogger("celery.task")
    logger.error(
        "===> This is sample celery task: arg=%s, kwarg=%s", arg, kwargs
    )
    return arg


# pylint: disable=unused-argument
# pylint: disable=import-outside-toplevel
@setup_logging.connect
def config_loggers(*args, **kwags):
    from logging.config import dictConfig
    from main.settings import celeryconfig

    dictConfig(celeryconfig.LOGGING)
