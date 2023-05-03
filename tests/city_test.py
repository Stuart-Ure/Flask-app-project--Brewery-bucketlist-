import unittest

from models.city import City
from models.brewery import Brewery

class TestCity(unittest.TestCase):
    def test_init(self):
        city1 = City("Edinburgh", 1)
        self.assertEqual(city1.name, "Edinburgh")


    def test_id(self):
        city2= City("Wellington",2)
        self.assertEqual(city2.id, 2)
        city2.id = 4
        self.assertEqual(city2.id, 4)