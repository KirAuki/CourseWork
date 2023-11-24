from rest_framework.viewsets import ModelViewSet
from ports.serializers import DeparturePortsSerializer, ArrivalPortsSerializer
from ports.models import DeparturePort, ArrivalPort
from django.db.models import Q

class DeparturePortsViewSet(ModelViewSet):
    queryset = DeparturePort.objects.filter(
    Q(name__startswith='A') | Q(country__startswith='A'))
    serializer_class = DeparturePortsSerializer

class ArrivalPortsViewSet(ModelViewSet):
    queryset = ArrivalPort.objects.all()
    serializer_class = ArrivalPortsSerializer

