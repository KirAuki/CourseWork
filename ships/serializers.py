from rest_framework import serializers
from ships.models import Ship

class ShipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = '__all__'