from celery.decorators import task
from celery import shared_task
from celery.utils.log import get_task_logger
from django.db import connection, connections
from django_globals import globals
from app.celery import app
import sys
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from django.conf import settings

import time
import json
from datetime import datetime, timedelta

from .models import *
from .mail import Notifications

@app.task(name="send_notiication")
def send_notifications():
    dt = datetime.now().replace(minute=30, second=0, microsecond=0)
    schedules = Schedule.objects.filter( message_status = 'New', send_at__lte = dt).order_by(id)[:settings.SEND_LIMIT]
    schedule_ids = [s.id for s in schedules]
    chats = Chat.objects.filter( id__in = schedule_ids, status = 1)
    n = Notifications()
    for chat in chats:
        n.send_notification(chat)
    Schedule.objects.filter(id__in = schedule_ids).update(message_status="Sent")

    return True