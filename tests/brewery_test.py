import unittest

from models.city import *
from models.brewery import Brewery

class TestBrewery(unittest.TestCase):


    def test_init(self):
        brewery1 = Brewery("Newbarns Brewery", "Edinburgh", True, 1)
        self.assertEqual(brewery1.name, "Newbarns Brewery")
        self.assertEqual(brewery1.city, "Edinburgh")
        self.assertEqual(brewery1.visited, True)
        self.assertEqual(brewery1.id, 1)

    def test_visited(self):
        brewery2 = Brewery("Moonwake", "Edinburgh", True, 2)
        self.assertTrue(brewery2.visited)
        brewery2.visited = True
        self.assertTrue(brewery2.visited)


    def test_id(self):
        brewery3 = Brewery("Heyday Brewery", "Wellington", False, 3)
        self.assertEqual(brewery3.id, 3)
        brewery3.id = 4
        self.assertEqual(brewery3.id, 4)
