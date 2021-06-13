import json
import datetime

import pytz
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django_celery_beat.models import (CrontabSchedule, IntervalSchedule,
                                       PeriodicTask)


def create_interval_task():
    # step 1: create interval schedule
    interval_schedule_every_10_seconds, created = IntervalSchedule.objects.get_or_create(
        every=10, period=IntervalSchedule.SECONDS,  # MICROSECONDS MINUTES HOURS DAYS
    )

    # step2 : create periodic task, this task appropriate with sample-task-run-10-seconds in celeryconfig.py
    task_name = "INTERVAL-10s_______DJANGO_CELERY_BEAT"
    periodic_task = PeriodicTask.objects.create(
        interval=interval_schedule_every_10_seconds,  # we created this above.
        name=task_name,  # simply describes this periodic task.
        task="main.celery_app.sample_task",  # name of task.
        args=json.dumps([task_name, "arg1", "arg2"]),
        kwargs=json.dumps({"be_careful": True,}),
        expires=timezone.now() + datetime.timedelta(seconds=30),
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
        # timezone=pytz.timezone("Canada/Pacific"),     # run this task every minute at timezone of Canada/Pacific
    )

    # step 2: create cron task, this task appropriate with task-run-every-6-hour in celeryconfig.py
    task_name = "CRON-1minute_______DJANGO_CELERY_BEAT"
    periodic_task = PeriodicTask.objects.create(
        crontab=cron_schedule_execute_every_minute,
        name=task_name,
        task="main.celery_app.sample_task",
        args=json.dumps([task_name, "arg1", "arg2"]),
        kwargs=json.dumps({"be_careful": True,}),
    )


def create_cron_task_run_at_timezone_Asia_Ho_Chi_Minh(asia_hcm_hour):
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute="*",
        hour=str(asia_hcm_hour),
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
        timezone=pytz.timezone("Asia/Ho_Chi_Minh"),     # celeryconfig: enable_utc = True (default), timezone = "utc" (default)
    )

    task_name = "CRON_Asia/Ho_Chi_Minh___DJANGO_CELERY_BEAT"
    PeriodicTask.objects.create(
        crontab=schedule,
        name=task_name,
        task="main.celery_app.sample_task",
        args=json.dumps([task_name,]),
    )


def create_cron_task_run_at_timezone_utc(utc_hour):
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute="*",
        hour=str(utc_hour),
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
        # timezone=,        # <== default is UTC
    )

    task_name = "CRON_UTC___DJANGO_CELERY_BEAT"
    PeriodicTask.objects.create(
        crontab=schedule,
        name=task_name,
        task="main.celery_app.sample_task",
        args=json.dumps([task_name,]),
    )


def create_cron_task_base_timezone():
    """
        Explain:
            if config in file celeryconfig.py
                enable_utc = True     
                timezone = "utc"

                if  current hour:
                    utc_hour = 8
                    asia_hcm_hour = 15

                ==> both tasks CRON_UTC___DJANGO_CELERY_BEAT and CRON_Asia/Ho_Chi_Minh___DJANGO_CELERY_BEAT 
                    will run at same time
            
            ----------------------------------------------------------------

            if config in file celeryconfig.py
                enable_utc = False         
                timezone = "Asia/Ho_Chi_Minh"

                if  current hour:
                    utc_hour = 8
                    asia_hcm_hour = 15

                ==> only CRON_Asia/Ho_Chi_Minh___DJANGO_CELERY_BEAT run at this time
                    CRON_UTC___DJANGO_CELERY_BEAT will run at time of UTC
    """

    utc_hour = datetime.datetime.now(datetime.timezone.utc).hour
    asia_hcm_hour = datetime.datetime.now(datetime.timezone.utc).astimezone(pytz.timezone('Asia/Ho_Chi_Minh')).hour
    print("utc_hour: ", utc_hour)
    print("asia_hcm_hour: ", asia_hcm_hour)
    create_cron_task_run_at_timezone_utc(utc_hour)
    create_cron_task_run_at_timezone_Asia_Ho_Chi_Minh(asia_hcm_hour)

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            # create_interval_task()
            # create_cron_task()
            create_cron_task_base_timezone()
        except Exception as e:
            raise CommandError('Create celery periodic task failed: "%s"' % e)

        self.stdout.write(
            self.style.SUCCESS("=========== finished command =======================")
        )
