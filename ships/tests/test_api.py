from django.urls import reverse
from ships.serializers import ShipsSerializer
from rest_framework.test import APITestCase
from ships.models import Ship


class ShipsApiTestCase(APITestCase):
    def test_get(self):
        Ship_1 = Ship.objects.create(name = 'Test Ship 1', capacity = '80000', status = 'Готов')
        Ship_2 = Ship.objects.create(name = 'Test Ship 2', capacity = '80000', status = 'Готов')
        url = reverse('ship-list')
        response = self.client.get(url)
        serializer_data = ShipsSerializer([Ship_1,Ship_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        print(response.data)


