from db.run_sql import run_sql
from models.city import City
from models.brewery import Brewery

import repositories.brewery_repository as brewery_repo

def save(city):
    sql = "INSERT INTO cities (name) VALUES ( %s) RETURNING id"
    values = [city.name,]
    results = run_sql( sql, values )
    city.id = results[0]['id']
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['id'])
        cities.append(city)
    return cities

def select_by_id(id):
    city= None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = City(result['name'], result['id'] )
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql) 