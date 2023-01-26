from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json

class MenuViewTest(TestCase):
  def setUp(self):
      self.menu1 = Menu.objects.create(id=1, title="Pizza", price=12.99, inventory=2)
      self.menu2 = Menu.objects.create(id=2, title="Pasta", price=9.99, inventory=1)
      self.menu3 = Menu.objects.create(id=3, title="Salad", price=7.99, inventory=4)

  def test_getall(self):
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)
    json_data = json.dumps(serializer.data)
    expected_result = json.dumps([{
      "id": 1,
      "title": "Pizza",
      "price": "12.99",
      "inventory": 2
    },
    {
      "id": 2,
      "title": "Pasta",
      "price": "9.99",
      "inventory": 1
    },
    {
      "id": 3,
      "title": "Salad",
      "price": "7.99",
      "inventory": 4
    }])
    self.assertEquals(json_data, expected_result)