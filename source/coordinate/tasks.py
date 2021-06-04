import datetime
import logging

from celery import shared_task
from coordinate.models import Coordinate
from coordinate.gmail_utility import send_gmail

logger = logging.getLogger("celery.task")


@shared_task
def check_battery_level():
    latest_coordinate = Coordinate.objects.all().order_by("-created_at").first()
    logger.debug("current battery level: %s", latest_coordinate.battery_level)
    if (
        latest_coordinate.battery_level <= 20
        or (datetime.datetime.now().astimezone() - latest_coordinate.created_at).seconds > 300
    ):
        sent_subject = "Battery low or missing battery data"
        sent_text = "battery level: {} at {}".format(
            latest_coordinate.battery_level, latest_coordinate.created_at
        )
        send_gmail(sent_subject, sent_text)
        logger.error("Send email at %s", datetime.datetime.now())
        print('----------')
    return None
