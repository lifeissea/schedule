from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"
