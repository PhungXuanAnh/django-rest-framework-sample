# pylint: disable=invalid-name
import os

import environ
from celery.schedules import crontab
from django.conf import settings
from kombu import Queue

env = environ.Env()

HIGH_QUEUE = "queue-high"
MEDIUM_QUEUE = "queue-medium"
LOW_QUEUE = "queue-low"

HIGH_ROUTE_KEY = "queue-high.priority"
MEDIUM_ROUTE_KEY = "queue-medium.priority"
LOW_ROUTE_KEY = "queue-low.priority"

# broker_url = "redis://{}:{}/2".format(
#     env("REDIS_HOST", default="127.0.0.1"), env("REDIS_PORT", default="6379")
# )

# broker_url = "amqp://rabbitmq:5672"
# broker_url = 'amqp://guest:guest@localhost:5672//'
broker_url = 'amqp://{user}:{password}@{host}:{port}//'.format(
    user=env("RABBITMQ_USER", default="guest"),
    password=env("RABBITMQ_PW", default="guest"),
    host=env("RABBITMQ_HOST", default="rabbitmq"),
    port=env("RABBITMQ_PORT", default="5672")
)

result_backend = 'rpc://'
result_persistent = False

# enable_utc = False              # default: True
# timezone = "Asia/Ho_Chi_Minh"   # default: 'utc'

accept_content = ["json"]

task_serializer = "json"
result_serializer = "json"

# Config Celery queue
task_default_queue = MEDIUM_QUEUE
task_create_missing_queues = True
broker_transport_options = {"queue_order_strategy": "sorted"}

task_queues = (
    Queue(HIGH_QUEUE),
    Queue(MEDIUM_QUEUE),
    Queue(LOW_QUEUE),
)

task_time_limit = 5 * 60
task_soft_time_limit = 60
task_interval = 10  # seconds

task_routes = {
    "main.celery_app.sample_task": {"queue": LOW_QUEUE, "routing_key": LOW_ROUTE_KEY,},
    "music.tasks.sample_music_task": {"queue": HIGH_QUEUE, "routing_key": HIGH_ROUTE_KEY,},
}

interval_task_name = "INTERVAL-10s_______celeryconfig.py"
cron_task_name = "CRON-1minute_______celeryconfig.py"
beat_schedule = {
    interval_task_name: {
        "task": "main.celery_app.sample_task",
        "schedule": task_interval,
        'args': (interval_task_name,)
    },
    # NOTE: min value of cron task is minute, if you want to specify second, do in your code
    # see example of cron configuration here:
    # https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules
    # to test your setup using method crontab_parse, see below link:
    # https://docs.celeryproject.org/en/stable/reference/celery.schedules.html#celery.schedules.crontab_parser
    # cron_task_name: {
    #     "task": "main.celery_app.sample_task",
    #     "schedule": crontab(minute='*'),
    #     'args': (cron_task_name,)
    # },
    cron_task_name: {
        "task": "music.tasks.sample_music_task",
        "schedule": crontab(minute='*'),
    },
    # "apply-pending-update-preferred-area": {
    #     "task": "cantec.apply_pending_update_preferred_area",
    #     "schedule": crontab(minute=0, hour="*"),
    # },
    # "clean-user-current-geo-location": {
    #     "task": "cantec.clean_user_current_geo_location",
    #     "schedule": crontab(minute="*/30"),
    # },
    # "add-number-online-vehicle": {
    #     "task": "cantec.add_number_online_vehicle",
    #     "schedule": crontab(hour="*/12"),
    # },
    # "conclude-daily-payment": {
    #     "task": "cantec.conclude_daily_payment",
    #     "schedule": crontab(minute=0, hour="*"),
    # },
    # "apply-pending-commission-rate": {
    #     "task": "cantec.apply_pending_commission_rate",
    #     "schedule": crontab(minute=0, hour=12),
    # },
}


LOGGING_DIR = os.path.join(settings.BASE_DIR, "logs")
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            # pylint: disable=line-too-long
            "format": "[%(asctime)s] [%(name)s] %(levelname)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s"
        },
        "simple": {"format": "[%(asctime)s] %(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {"level": "INFO", "class": "logging.StreamHandler", "formatter": "verbose",},
        "celery.beat.FILE": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGING_DIR + "/celery.beat.log",
            "formatter": "verbose",
            "mode": "a",
            "maxBytes": 50 * 1024 * 1024,  # 50M
            "backupCount": 3,
        },
        "celery.worker.FILE": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGING_DIR + "/celery.worker.log",
            "formatter": "verbose",
            "mode": "a",
            "maxBytes": 50 * 1024 * 1024,  # 50M
            "backupCount": 3,
        },
        "celery.task.FILE": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGGING_DIR + "/celery.task.log",
            "formatter": "verbose",
            "mode": "a",
            "maxBytes": 50 * 1024 * 1024,  # 50M
            "backupCount": 3,
        },
    },
    "loggers": {
        "celery.worker": {
            "handlers": ["console", "celery.worker.FILE"],
            "level": "INFO",
            "propagate": True,
        },
        "celery.beat": {
            "handlers": ["console", "celery.beat.FILE"],
            "level": "INFO",
            "propagate": True,
        },
        "celery.task": {
            "handlers": ["console", "celery.task.FILE"],
            "level": "INFO",
            "propagate": True,
        }
    },
}
