from rest_framework import serializers
from containers.models import Container
from schedules.models import Schedule


class SchedulesSerializerForContainer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ContainersSerializer(serializers.ModelSerializer):
    schedule = SchedulesSerializerForContainer(read_only = True)
    class Meta:
        model = Container
        fields = '__all__'      
    
    def create(self, validated_data):
        return Container.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.schedule = validated_data.get('schedule', instance.schedule)
        instance.size = validated_data.get('size', instance.size)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()
        return instance