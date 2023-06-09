from rest_framework import serializers
from ports.models import DeparturePort,ArrivalPort 

class DeparturePortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeparturePort
        fields = '__all__'

class ArrivalPortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArrivalPort
        fields = '__all__'