import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from django.shortcuts import reverse
from conftest import EVERYTHING_EQUALS_NOT_NONE


pytestmark = [pytest.mark.django_db]


class TestGuestEndpoints(APITestCase):
    fixtures = ['catalog/tests/fixtures/categories_fixture.json']
    def test_categories_list_endpoints(self):
        url = reverse('categories')
        responce = self.client.get(url)
        assert responce.status_code == 200
        assert isinstance(responce.data, list)
        assert responce.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 2,
                "name":EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 3,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE
            },
        ]

class TestCategoriesView(APITestCase):
    fixtures = [
        'catalog/tests/fixtures/products_fixtures.json',
        'catalog/tests/fixtures/sellers_fixtures.json',
        'catalog/tests/fixtures/discounts_fixtures.json',
        'catalog/tests/fixtures/categories_fixture.json'
    ]

    def test_categories_view(self):
        url = reverse('category-product', kwargs={'category_id': 0})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

        expected_data = [
            {
                "id": 1,
                "name": "╠ръёшь ├рыъшэ",
                "article": "25841256",
                "description": "dfghjkewsdfghjkredfghjk,lkjgfrdfh",
                "count_on_stock": 1,
                "price": "25.00",
                "discount": None,
                "category": None,
                "seller": {
                    "id": 1,
                    "name": "─шы■ъ ╨рэутшэфЁ",
                    "description": "dfghjkl;",
                    "contact": "fghnjkl.;"
                }
            },
            {
                "id": 2,
                "name": "─шы■ъ ╨рэутшэфЁ",
                "article": "52463236",
                "description": "dsfghjkhgfdsdfghmn,",
                "count_on_stock": 3,
                "price": "35.00",
                "discount": None,
                "category": {
                    "id": 2,
                    "name": "EVERYTHING_EQUALS_NOT_NONE",
                    "description": "EVERYTHING_EQUALS_NOT_NONE"
                },
                "seller": {
                    "id": 1,
                    "name": "─шы■ъ ╨рэутшэфЁ",
                    "description": "dfghjkl;",
                    "contact": "fghnjkl.;"
                }
            },
            {
                "id": 3,
                "name": "╦хюэшф ╚ы№шў",
                "article": "2364125412",
                "description": "gfcdeswdctghbjnkmjnhbvgfrde",
                "count_on_stock": 4,
                "price": "752.00",
                "discount": None,
                "category": {
                    "id": 2,
                    "name": "EVERYTHING_EQUALS_NOT_NONE",
                    "description": "EVERYTHING_EQUALS_NOT_NONE"
                },
                "seller": {
                    "id": 1,
                    "name": "─шы■ъ ╨рэутшэфЁ",
                    "description": "dfghjkl;",
                    "contact": "fghnjkl.;"
                }
            },
            {
                "id": 4,
                "name": "Pantsu",
                "article": "852145",
                "description": "dfcgvnmkl",
                "count_on_stock": 1000,
                "price": "3.00",
                "discount": {
                    "id": 1,
                    "name": "HappyNewYear",
                    "percent": 30,
                    "date_start": "2024-03-17T17:41:53Z",
                    "date_end": "2024-05-08T17:41:59Z"
                },
                "category": {
                    "id": 1,
                    "name": "EVERYTHING_EQUALS_NOT_NONE",
                    "description": "EVERYTHING_EQUALS_NOT_NONE"
                },
                "seller": {
                    "id": 1,
                    "name": "─шы■ъ ╨рэутшэфЁ",
                    "description": "dfghjkl;",
                    "contact": "fghnjkl.;"
                }
            }
        ]

