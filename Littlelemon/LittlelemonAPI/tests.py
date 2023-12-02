from django.test import TestCase
from django.urls import reverse
from .models import(
    MenuAPI,
) 
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
class MenuAPITest(TestCase):
    def test_get_item(self):
        item = MenuAPI.objects.create(title="Rice", price=80, inventory=12)
        self.assertEqual(str(item), "Rice : 80")

class MenuAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # test for creating a new menu item
        self.item1 = MenuAPI.objects.create(title="Burger", price=10, inventory=50)
        self.item2 = MenuAPI.objects.create(title="Pizza", price=15, inventory=30)

    def test_test_details(self):
        """
        This method tests the details view of an individual menu item
        """
        url = reverse('menu-detail', kwargs={'pk': self.item1.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)