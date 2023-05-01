from db.run_sql import run_sql
from models.city import City
from models.brewery import Brewery
import repositories.city_repository as city_repo


def save(brewery):
    sql = "INSERT INTO breweries ( name, city_id, visited) VALUES ( %s, %s, %s) RETURNING id"
    values = [brewery.name, brewery.city.id, brewery.visited]
    results = run_sql( sql, values )
    brewery.id = results[0]['id']
    return brewery


def select_all():
    breweries= []

    sql = "SELECT * FROM breweries"
    results = run_sql(sql)

    for row in results:
        city = city_repo.select_by_id(row['city_id'])
        brewery= Brewery(row['name'], city, row['id'])
        breweries.append(brewery)
    return breweries


def select(id):
    brewery = None
    sql = "SELECT * FROM breweries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    
    if result is not None:
        city=city_repo.select_by_id(result['city_id'])
        brewery= Brewery(result['name'], city, result['id'])
    return brewery

def delete_all():
    sql = "DELETE FROM breweries"
    run_sql(sql)