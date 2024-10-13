import json

from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from .models import Menu
from .views import MenuViewSet


# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=2, title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(id=2, title="IceCream", price=80, inventory=100)
        Menu.objects.create(id=3, title="Cake", price=20, inventory=50)

    def test_getall(self):
        menus = Menu.objects.all()
        response: HttpResponse = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), len(menus))


