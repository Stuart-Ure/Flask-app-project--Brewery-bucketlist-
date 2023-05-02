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
        brewery= Brewery(row['name'], city, row['visited'], row['id'])
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

def delete_by_id(id):
    sql = "DELETE FROM breweries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# THE BELOW IS THE UPDATE THAT I CANT GET TO WORK
# def update(brewery):
#     sql = "UPDATE breweries SET (name, city_id, visited, VALUES) = (%s, %s, %s) WHERE id = %s"
#     values = [brewery.name, brewery.city.id, brewery.visited]
#     results = run_sql( sql, values )
#     brewery.id = results[0]['id']
#     return brewery




# ......THE BELOW IS TO  SHOW ALL BREWERIES BY CITY ON A NEW PAGE

# def brewery_by_city(city):
#     brewery = []

#     sql = "SELECT * FROM brewery WHERE city_id = %s"
#     values = [city.id]
#     results = run_sql(sql, values)

#     for row in results:
#         brewery = Brewery (row ['name'], row['city'], row['visited'], row['id'] )
#         brewery.append(brewery)
#     return brewery