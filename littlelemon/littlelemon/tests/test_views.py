import json

from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(id=2, title="IceCream", price=80, inventory=100)
        Menu.objects.create(id=3, title="Cake", price=20, inventory=50)

    def test_getall(self):
        menus = Menu.objects.all()
        response: HttpResponse = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), len(menus))
