from rest_framework.viewsets import ModelViewSet
from ports.serializers import DeparturePortsSerializer, ArrivalPortsSerializer
from ports.models import DeparturePort, ArrivalPort


class DeparturePortsViewSet(ModelViewSet):
    queryset = DeparturePort.objects.all()
    serializer_class = DeparturePortsSerializer

class ArrivalPortsViewSet(ModelViewSet):
    queryset = ArrivalPort.objects.all()
    serializer_class = ArrivalPortsSerializer

