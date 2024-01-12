from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from containers.serializers import ContainersSerializer
from containers.models import Container
from .forms import AddContainerForm
from django.db.models import Q
from django.shortcuts import redirect ,render

class ContainersViewSet(ModelViewSet):
    # queryset = Container.objects.filter((Q(size='12x2x2.5') | Q(weight=1250.0)) & ~Q(done=True))
    queryset = Container.objects.all()
    serializer_class = ContainersSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['name', 'done']
    ordering_fields = ['weight']


def add_container(request):

    if request.method == 'POST':
        form = AddContainerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('')
            except:
                form.add_error(None, "Ошибка добавления контейнера")
    else:
        form = AddContainerForm(request.POST)


    form = AddContainerForm()
    return render(request, 'containers/add_container.html', {'form': form,})