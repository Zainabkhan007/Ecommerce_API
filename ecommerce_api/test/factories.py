import factory
from api.models import *

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name=factory.Sequence(lambda n: 'Category_%d' % n)

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
    name=factory.Sequence(lambda n: 'Brand_%d' % n)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    name='test_product'
    description='description_test'
    is_digital=True
    brand=factory.SubFactory(BrandFactory)
    category=factory.SubFactory(CategoryFactory)


