from rest_framework.viewsets import ModelViewSet
from ships.serializers import ShipsSerializer
from ships.models import Ship


class ShipsViewSet(ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipsSerializer
