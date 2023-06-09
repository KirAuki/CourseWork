from rest_framework import serializers
from routes.models import Route
from ports.models import DeparturePort,ArrivalPort 

class DeparturePortsSerializerForRoute(serializers.ModelSerializer):
    class Meta:
        model = DeparturePort
        fields = ['name']

class ArrivalPortsSerializerForRoute(serializers.ModelSerializer):
    class Meta:
        model = ArrivalPort
        fields = ['name']


class RoutesSerializer(serializers.ModelSerializer):
    departurePort_data = DeparturePortsSerializerForRoute(source='departure')
    arrivalPort_data = ArrivalPortsSerializerForRoute(source='arrival')
    class Meta:
        model = Route
        exclude = ['arrival','departure']