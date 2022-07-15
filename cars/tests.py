from django.test import TestCase,Client

from .models import brand,Cars

# Create your tests here.

class CarsTest(TestCase):

    def setUp(self):
        m1 = brand.objects.create(name='Pros')
        m2 = brand.objects.create(name='bb')
        m2 = brand.objects.create(name='bxb')
        c1 = Cars.objects.create(modeli='Elly',probeg=125,comment='Best Car ever',brand=m1)

    def test_valid_milage(self):
        ca = Cars.objects.get(modeli='Elly')
        self.assertTrue(ca.is_valid_milage())    
    def test_brands(self):
        c = Client()
        res = c.get('/brands/')
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.context['brand_list'].count(),3)