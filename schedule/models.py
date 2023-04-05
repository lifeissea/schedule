from asyncio import AbstractServer
from typing import AbstractSet
from django.db import models

from common.models import CommonModel
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Schedule(CommonModel):
    """Schedule Model Definition"""

    content = models.TextField()
    date = models.DateField()
    starttime = models.PositiveIntegerField()
    endtime = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


class ScheduleDetail(CommonModel):
    """ScheduleDetail Model Definition"""

    schedule = models.ForeignKey(
        "Schedule", related_name="schedule_detail", on_delete=models.CASCADE
    )
    content = models.TextField()
    date = models.DateField()
    starttime = models.PositiveIntegerField()
    endtime = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
