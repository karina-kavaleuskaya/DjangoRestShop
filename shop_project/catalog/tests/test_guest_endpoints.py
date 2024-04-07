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
        'catalog/tests/fixtures/categories_fixture.json',
        'catalog/tests/fixtures/productimages_fixtures.json',
    ]

    def test_sellers_list(self):
        url = reverse('sellers')
        responce = self.client.get(url)
        assert responce.status_code == 200
        assert isinstance(responce.data, list)
        assert responce.data == [
            {
                "id": 1,
                "name": "─шы■ъ ╨рэутшэфЁ",
                "description": "dfghjkl;",
                "contact": "fghnjkl.;"
            }
        ]

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


    def test_discounts_list(self):
        url = reverse('discounts')
        responce = self.client.get(url)
        assert responce.status_code == 200
        assert isinstance(responce.data, list)
        assert responce.data == [
            {
                "id": 1,
                "name": "HappyNewYear",
                "percent": 30,
                "date_start": "2024-03-17T17:41:53Z",
                "date_end": "2024-05-08T17:41:59Z"
            },
            {
                "id": 2,
                "name": "Aboba",
                "percent": 60,
                "date_start": "2024-04-01T17:42:13Z",
                "date_end": "2024-04-01T17:42:14Z"
            }
        ]

        def test_category_products(self):
            url = reverse('category-products', kwargs={'category_id': 1})
            response = self.client.get(url)

            assert response.status_code == 200
            assert response.data == [
                {
                    "id": 5,
                    "name": EVERYTHING_EQUALS_NOT_NONE,
                    "price": "50.00",
                    "article": EVERYTHING_EQUALS_NOT_NONE,
                    "description": EVERYTHING_EQUALS_NOT_NONE,
                    "count_on_stock": EVERYTHING_EQUALS_NOT_NONE,
                    "discount": EVERYTHING_EQUALS_NOT_NONE,
                    "category": EVERYTHING_EQUALS_NOT_NONE,
                    "seller": EVERYTHING_EQUALS_NOT_NONE,
                    "images": EVERYTHING_EQUALS_NOT_NONE
                }
            ]
            assert response.data[0]["discount"] == {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "percent": 30,
                "date_start": EVERYTHING_EQUALS_NOT_NONE,
                "date_end": EVERYTHING_EQUALS_NOT_NONE
            }
            assert response.data[0]["images"] == {
                "id": 4,
                "product": 4,
                "image": EVERYTHING_EQUALS_NOT_NONE
            }




