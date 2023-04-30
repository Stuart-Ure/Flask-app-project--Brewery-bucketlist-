from db.run_sql import run_sql
from models.city import City
from models.brewery import Brewery

def save(city):
    sql = "INSERT INTO city(name) VALUES ( %s) RETURNING id"
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

def select(id):
    city= None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = City(result['name'], result['id'] )
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql) 