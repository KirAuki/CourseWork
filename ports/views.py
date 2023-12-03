from rest_framework.viewsets import ModelViewSet
from ports.serializers import DeparturePortsSerializer, ArrivalPortsSerializer
from ports.models import DeparturePort, ArrivalPort
from rest_framework import filters

class DeparturePortsViewSet(ModelViewSet):
    queryset = DeparturePort.objects.all()
    serializer_class = DeparturePortsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'country']

class ArrivalPortsViewSet(ModelViewSet):
    queryset = ArrivalPort.objects.all()
    serializer_class = ArrivalPortsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'country']

