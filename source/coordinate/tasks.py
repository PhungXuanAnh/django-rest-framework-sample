import datetime
import logging
import pytz

from celery import shared_task
from coordinate.models import Coordinate
from coordinate.gmail_utility import send_gmail

logger = logging.getLogger("celery.task")


@shared_task
def check_battery_level():
    latest_coordinate = Coordinate.objects.all().order_by("-created_at").first()
    logger.debug("current battery level: %s", latest_coordinate.battery_level)

    if (
        not latest_coordinate.battery_level
        or (datetime.datetime.now().astimezone() - latest_coordinate.created_at).seconds > 300
    ):
        sent_subject = "Missing battery data"
        sent_text = "Last data at {}".format(
            latest_coordinate.created_at.astimezone(pytz.timezone("Asia/Ho_Chi_Minh")).strftime("[%Y-%m-%d]-[%H:%M:%S]")
        )
        send_gmail(sent_subject, sent_text)
        logger.error("Send email at %s", datetime.datetime.now())
        return None

    if latest_coordinate.battery_level <= 30:
        sent_subject = "Battery low"
        sent_text = "battery level: {} at {}".format(
            latest_coordinate.battery_level,
            latest_coordinate.created_at.astimezone(pytz.timezone("Asia/Ho_Chi_Minh")).strftime("[%Y-%m-%d]-[%H:%M:%S]"),
        )
        send_gmail(sent_subject, sent_text)
        logger.error("Send email at %s", datetime.datetime.now())
    return None
