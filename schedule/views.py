import datetime
from django.shortcuts import render
from dateutil.parser import parse as parse_date

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from dateutil import parser

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer

# Create your views here.
class ScheduleView(APIView):
    def get(self, request):
        date_str = request.query_params.get('date')
        if date_str:
            try:
                date = parser.parse(date_str).date()
            except ValueError:
                return Response({'error': 'Invalid date format.'}, status=400)
            schedules = Schedule.objects.filter(date=date)
        else:
            schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        date_str = data.get('date')
        if date_str:
            data['date'] = parse_date(date_str).strftime('%Y-%m-%d')
        serializer = ScheduleSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class ScheduleDetailView(APIView):
    def get_object(self, pk):
        try:
            return Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)

    def put(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerializer(schedule, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        schedule.delete()
        return Response({"message": "Schedule has been deleted."})
