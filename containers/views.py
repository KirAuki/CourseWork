from rest_framework.viewsets import ModelViewSet
from containers.serializers import ContainersSerializer
from containers.models import Container


class ContainersViewSet(ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainersSerializer
