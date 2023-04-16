# serializers.py

from rest_framework import serializers
from schedule.models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = Schedule
        fields = '__all__'
