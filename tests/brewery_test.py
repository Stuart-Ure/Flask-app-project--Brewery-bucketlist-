# import unittest

# from models.city import City
# from models.brewery import Brewery
# import repositories.city_repository as city_repo
# import repositories.brewery_repository as brewery_repo

# class Testbrewery_repo(unittest.TestCase):

    # def setUp(self):
    #     self.city_repo = city_repo()
    #     self.brewery_repo = brewery_repo()

    #     # Delete all cities and breweries from the database
    #     self.brewery_repo.delete_all()
    #     self.city_repo.delete_all()

    #     # Create some cities and breweries for testing
    #     self.city1 = City("Edinburgh")
    #     self.city_repo.save(self.city1)

    #     self.city2 = City("Wellington")
    #     self.city_repo.save(self.city2)

    #     self.brewery1 = Brewery("Newbarns Brewery", self.city1, True)
    #     self.brewery_repo.save(self.brewery1)

    #     self.brewery2 = Brewery("Moonwake Brewery", self.city1, False)
    #     self.brewery_repo.save(self.brewery2)

    #     self.brewery3 = Brewery("Heyday Brewery", self.city2, False)
    #     self.brewery_repo.save(self.brewery3)

    #     self.brewery4 = Brewery("Fortune Favours", self.city2, True)
    #     self.brewery_repo.save(self.brewery4)

    # def delete_all(self):
    #     # Delete all cities and breweries from the database after each test
    #     self.brewery_repo.delete_all()
    #     self.city_repo.delete_all()

    # def test_save(self):
    #     # Create a new brewery and save it to the database
    #     city3 = City("Portland")
    #     self.city_repo.save(city3)

    #     brewery5 = Brewery("Brewery Five", city3, True)
    #     self.brewery_repo.save(brewery5)

    #     # Check that the brewery has been assigned an ID by the database
    #     self.assertIsNotNone(brewery5.id)

    #     # Check that the saved brewery matches the expected values
    #     saved_brewery = self.brewery_repo.select(brewery5.id)
    #     self.assertEqual(brewery5.name, saved_brewery.name)
    #     self.assertEqual(brewery5.city.id, saved_brewery.city.id)
    #     self.assertEqual(brewery5.visited, saved_brewery.visited)

    # def test_select_all(self):
    #     # Retrieve all breweries from the database
    #     breweries = self.brewery_repo.select_all()

    #     # Check that the number of retrieved breweries matches the expected value
    #     self.assertEqual(len(breweries), 4)

    #     # Check that each retrieved brewery matches the expected values
    #     self.assertEqual(breweries[0].name, "Newbarns Brewery")
    #     self.assertEqual(breweries[0].city.name, "Edinburgh")
    #     self.assertEqual(breweries[0].visited, True)

    #     self.assertEqual(breweries[1].name, "Moonwake Brewery")
    #     self.assertEqual(breweries[1].city.name, "Edinburgh")
    #     self.assertEqual(breweries[1].visited, False)

    #     self.assertEqual(breweries[2].name, "Heyday Brewery")
    #     self.assertEqual(breweries[2].city.name, "Wellington")
    #     self.assertEqual(breweries[2].visited, False)

    #     self.assertEqual(breweries[3].name, "Fortune Favours")
    #     self.assertEqual(breweries[3].city.name, "Wellington")
    #     self.assertEqual(breweries[3].visited, True)

    # def test_select(self):
    #     # Retrieve a single brewery from the database
    #     brewery = self.brewery_repo.select
