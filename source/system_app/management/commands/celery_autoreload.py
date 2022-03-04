import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload

# Reference: https://stackoverflow.com/a/49166246/7639845
#           https://www.accordbox.com/blog/how-auto-reload-celery-worker-code-change/


def restart_celery():
    cmd = "pkill celery"
    subprocess.call(shlex.split(cmd))
    cmd = "celery -A user_portal worker -l INFO -Q email,sms,slack,mobile_notification,common,report_json_uploader,update_payment_request_status"
    subprocess.call(shlex.split(cmd))


def restart_celery_with_debugpy():
    cmd = "ps -aux | grep debugpy | awk '{print $2}' | xargs kill -9"
    subprocess.run(cmd, shell=True)
    cmd = "python -m debugpy --listen 0.0.0.0:5679 -m celery -A user_portal worker -l INFO -Q email,sms,slack,mobile_notification,common,report_json_uploader,update_payment_request_status"
    subprocess.call(shlex.split(cmd))


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("=== Starting celery worker with autoreload...")

        # For Django>=2.2
        # autoreload.run_with_reloader(restart_celery)
        autoreload.run_with_reloader(restart_celery_with_debugpy)

        # For django<2.1
        # autoreload.main(restart_celery)
