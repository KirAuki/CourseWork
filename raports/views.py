from rest_framework.viewsets import ModelViewSet
from raports.serializers import RaportsSerializer
from raports.models import Raport


class RaportsViewSet(ModelViewSet):
    queryset = Raport.objects.all()
    serializer_class = RaportsSerializer

