from datetime import datetime, timedelta

from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Link

logger = get_task_logger(__name__)


@shared_task
def delete_overdue_links():
    logger.info(
        'Starting delete overdue short links'
    )
    last_allowed_date = datetime.now() - timedelta(days=1)
    links = Link.objects.exclude(created_at__gt=last_allowed_date)
    for link in links:
        link.delete()
    logger.info(
        'Task successfuly completed.'
    )
