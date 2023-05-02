from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.city import City
from models.brewery import Brewery
import repositories.brewery_repository as brewery_repo
import repositories.city_repository as city_repo

brewery_blueprint = Blueprint("brewery", __name__)

@brewery_blueprint.route("/breweries")
def breweries():
    brewery = brewery_repo.select_all() 
    cities = city_repo.select_all()
    return render_template("breweries/brewery.jinja", brewery = brewery, cities=cities)


@brewery_blueprint.route("/breweries/<id>")
def show(id):
    brewery = brewery_repo.select(id)
    return render_template("breweries/brewery.jinja", brewery = brewery)

@brewery_blueprint.route('/breweries/delete/<id>', methods=['POST'])
def delete_brewery(id):
    brewery_repo.delete_by_id(id)
    return redirect('/breweries')

@brewery_blueprint.route('/breweries', methods=['POST'])
def add_brewery():
    # get data from form
    name= request.form["name"] 
    cities= request.form ["city"]
    visited= request.form ["visited"]
    # make a city instance from form data
    city = city_repo.select_by_id(int(cities))
    if visited.lower() == 'true':
        visited = True
    else:
        visited =False
    brewery = Brewery (name,city,visited)
    # save the city using city repository
    brewery_repo.save(brewery)
    return redirect('/breweries')