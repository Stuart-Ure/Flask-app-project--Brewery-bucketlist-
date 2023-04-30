import pdb
from models.city import City
from models.brewery import Brewery

import repositories.city_repository as city_repo
import repositories.brewery_repository as brewery_repo

city_repo.delete_all()
brewery_repo.delete_all()

