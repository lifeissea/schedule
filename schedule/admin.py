from django.contrib import admin

from schedule.models import Schedule

# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
        "date",
        "startTime",
        "endTime",
    )
