from rest_framework import serializers
from schedules.models import Schedule
from ships.models import Ship
from routes.models import Route

class ShipsSerializerForSchedules(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = '__all__'
class RoutesSerializerForSchedules(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class SchedulesSerializer(serializers.ModelSerializer):
    ship_data = ShipsSerializerForSchedules(source='ship', many=True)
    route_data = RoutesSerializerForSchedules(source='route')
    class Meta:
        model = Schedule
        exclude = ['ship','route']

    def create(self, validated_data):
        return Schedule.objects.create(**validated_data)