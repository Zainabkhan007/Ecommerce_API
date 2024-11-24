import factory
import json
import pytest
pytestmark=pytest.mark.django_db



class TestCategoryEnpoints:
    endpoint='/api/category/'
    def test_get_category(self,category_factory,api_client):
        category_factory.create_batch(4)
        response=api_client().get(self.endpoint)
        assert response.status_code == 200
        # print(json.loads(response.content))
        assert len(json.loads(response.content))== 4


class TestBrandEnpoints:
    endpoint='/api/brand/'
    def test_get_brand(self,brand_factory,api_client):
        brand_factory.create_batch(4)
        response=api_client().get(self.endpoint)
        assert response.status_code == 200
        # print(json.loads(response.content))
        assert len(json.loads(response.content))== 4


class TestProductEnpoints:
    endpoint='/api/product/'
    def test_get_product(self,product_factory,api_client):
        product_factory.create_batch(4)
        response=api_client().get(self.endpoint)
        assert response.status_code == 200
        # print(json.loads(response.content))
        assert len(json.loads(response.content))== 4