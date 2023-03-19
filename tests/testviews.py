
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from restaurant.views import MenuItemsView

class MenuViewTest(APITestCase):
    def test_getall(self):
         item = {
              "title":"IceCream",
              "price":"80.00",
              "inventory":100
         }
         response = self.client.post(reverse("menu"),item)
         res= {
              "title":response.data["title"],
              "price":response.data["price"],
              "inventory":response.data["inventory"]
         }
         self.assertEqual(res,item)

