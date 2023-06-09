from rest_framework.routers import DefaultRouter
from containers.views import ContainersViewSet
from ports.views import DeparturePortsViewSet,ArrivalPortsViewSet
from raports.views import RaportsViewSet
from routes.views import RoutesViewSet
from schedules.views import SchedulesViewSet
from ships.views import ShipsViewSet
from authentication.views import UsersViewSet


router = DefaultRouter()

router.register('containers', ContainersViewSet)
router.register('departure_ports',DeparturePortsViewSet)
router.register('arrival_ports',ArrivalPortsViewSet)
router.register('raports',RaportsViewSet)
router.register('routes',RoutesViewSet)
router.register('schedules',SchedulesViewSet)
router.register('ships',ShipsViewSet)
router.register('auth',UsersViewSet)
