import pytest
from rest_framework.test import APITestCase
from django.shortcuts import reverse


pytestmark = [pytest.mark.django_db]


class TestGuestEndpoints(APITestCase):
    def test_categories_list_endpoints(self):
        url = reverse('categories')
        responce = self.client.get(url)
        assert responce.status_code == 200
        assert isinstance(responce.data, list)
        assert responce.data == []
