from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repo


cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repo.select_all() # NEW
    return render_template("cities/cities.jinja", cities = cities)

@cities_blueprint.route("/cities/<id>")
def show(id):
    cities = city_repo.select(id)

@cities_blueprint.route('/cities/delete/<id>', methods=['POST'])
def delete_city(id):
    city_repo.delete_by_id(int(id))
    return redirect('/cities')