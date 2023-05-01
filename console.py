import pdb
from models.city import City
from models.brewery import Brewery

import repositories.city_repository as city_repo
import repositories.brewery_repository as brewery_repo

brewery_repo.delete_all()
city_repo.delete_all()

city1 = City ("Edinburgh")
city_repo.save(city1)

city2= City ("Wellington")
city_repo.save(city2)

brewery1 = Brewery ("Newbarns Brewery", city1, True)
brewery_repo.save(brewery1)

brewery2 = Brewery ("Moonwake Brewery", city1, False)
brewery_repo.save(brewery2)

brewery3 = Brewery ("Heyday Brewery", city2, False)
brewery_repo.save(brewery3)

brewery4 = Brewery ("Fortune Favours", city2, True)
brewery_repo.save(brewery4)

# brewery1 = Brewery ("Newbarns Brewery", "Edinburgh")
# brewery_repo.save(brewery1)

# brewery2= Brewery ("Moonwake Brewery", "Edinburgh")
# brewery_repo.save(brewery2)

# brewery4 = Brewery ("Heyday Brewing" "Wellington")
# brewery_repo.save(brewery4)

# brewery5 = Brewery ("Garage Project" "Wellington")
# brewery_repo.save(brewery5)
