from rest_framework.viewsets import ModelViewSet
from schedules.serializers import SchedulesSerializer
from schedules.models import Schedule


class SchedulesViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = SchedulesSerializer
