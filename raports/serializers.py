from rest_framework import serializers
from raports.models import Raport
from schedules.models import Schedule

class SchedulesSerializerForRaports(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['name','departure_date','arrival_date']

class RaportsSerializer(serializers.ModelSerializer):
    schedule_data = SchedulesSerializerForRaports(source='schedule')
    class Meta:
        model = Raport
        exclude = ['schedule']