from rest_framework import serializers
from schedules.models import Schedule
from ships.models import Ship
from routes.models import Route

class ShipsSerializerForSchedules(serializers.ModelSerializer):
    class Meta:
        model = Ship
        exclude = ['capacity','status']
class RoutesSerializerForSchedules(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['name']

class SchedulesSerializer(serializers.ModelSerializer):
    ship_data = ShipsSerializerForSchedules(source='ship',read_only=True, many=True)
    route_data = RoutesSerializerForSchedules(source='route')
    class Meta:
        model = Schedule
        exclude = ['ship','route']