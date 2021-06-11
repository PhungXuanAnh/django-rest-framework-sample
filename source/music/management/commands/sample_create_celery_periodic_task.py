from django.core.management.base import BaseCommand, CommandError
import json
from datetime import timedelta
import pytz
from django_celery_beat.models import (CrontabSchedule, IntervalSchedule,
                                       PeriodicTask)
from django.utils import timezone



def create_interval_task():
    # step 1: create interval schedule
    interval_schedule_every_10_seconds, created = IntervalSchedule.objects.get_or_create(
        every=10, period=IntervalSchedule.SECONDS,  # MICROSECONDS MINUTES HOURS DAYS
    )

    # step2 : create periodic task, this task appropriate with sample-task-run-10-seconds in celeryconfig.py
    task_name = "INTERVAL-10s__DJANGO_CELERY_BEAT"
    periodic_task = PeriodicTask.objects.create(
        interval=interval_schedule_every_10_seconds,  # we created this above.
        name=task_name,  # simply describes this periodic task.
        task="main.celery_app.sample_task",  # name of task.
        args=json.dumps([task_name, "arg1", "arg2"]),
        kwargs=json.dumps({"be_careful": True,}),
        expires=timezone.now() + timedelta(seconds=30),
    )


    ## to temporary disable this task
    # periodic_task.enabled = False
    # periodic_task.save()


def create_cron_task():
    # NOTE: min value of cron task is minute, if you want to specify second, do in your code
    # see example of cron configuration here: 
    # https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules
    # to test your setup using method crontab_parse, see below link:
    # https://docs.celeryproject.org/en/stable/reference/celery.schedules.html#celery.schedules.crontab_parser
    # step 1: create cron schedule
    cron_schedule_execute_every_minute, _ = CrontabSchedule.objects.get_or_create(
        minute="*",
        hour="*",
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
        # timezone=pytz.timezone("Canada/Pacific"),
    )

    # step 2: create cron task, this task appropriate with task-run-every-6-hour in celeryconfig.py
    task_name = "CRON-1minute__DJANGO_CELERY_BEAT"
    periodic_task = PeriodicTask.objects.create(
        crontab=cron_schedule_execute_every_minute,
        name=task_name,
        task="main.celery_app.sample_task",
        args=json.dumps([task_name, "arg1", "arg2"]),
        kwargs=json.dumps({"be_careful": True,}),
    )


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            create_interval_task()
            create_cron_task()
        except Exception as e:
            raise CommandError('Create celery periodic task failed: "%s"' % e)

        self.stdout.write(
            self.style.SUCCESS("=========== finished command =======================")
        )
