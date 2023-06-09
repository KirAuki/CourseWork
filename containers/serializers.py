from rest_framework import serializers
from containers.models import Container
from schedules.models import Schedule


class SchedulesSerializerForContainer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['name']


class ContainersSerializer(serializers.ModelSerializer):
    schedule_data = SchedulesSerializerForContainer(source='schedule')
    class Meta:
        model = Container
        exclude = ['schedule']