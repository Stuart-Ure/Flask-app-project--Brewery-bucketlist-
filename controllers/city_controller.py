from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repo


city_blueprint = Blueprint("cities", __name__)

@city_blueprint.route("/cities")
def cities():
    cities = city_repo.select_all() # NEW
    return render_template("cities/index.jinja", cities = City)

@city_blueprint.route("/cities/<id>")
def show(id):
    city = city_repo.select(id)

    