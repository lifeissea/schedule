from django.db import models

from common.models import CommonModel


class Schedule(CommonModel):
    content = models.TextField()
    date = models.DateField()
    startTime = models.IntegerField()
    endTime = models.IntegerField()

    def __str__(self):
        return str(self.id)



class ScheduleDetail(CommonModel):
    """ScheduleDetail Model Definition"""

    schedule = models.ForeignKey(
        "Schedule", related_name="schedule_detail", on_delete=models.CASCADE
    )
    content = models.TextField()
    date = models.DateField()
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
