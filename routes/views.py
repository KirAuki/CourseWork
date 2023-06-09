from rest_framework.viewsets import ModelViewSet
from routes.serializers import RoutesSerializer
from routes.models import Route


class RoutesViewSet(ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RoutesSerializer

