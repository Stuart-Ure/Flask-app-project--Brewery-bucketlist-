from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.brewery import Brewery
import repositories.brewery_repository as brewery_repo

brewery_blueprint = Blueprint("brewery", __name__)

@brewery_blueprint.route("/breweries")
def breweries():
    brewery = brewery_repo.select_all() 
    return render_template("breweries/brewery.jinja", brewery = brewery)


@brewery_blueprint.route("/breweries/<id>")
def show(id):
    brewery = brewery_repo.select(id)
    return render_template("breweries/brewery.jinja", brewery = brewery)

@brewery_blueprint.route('/breweries/delete/<id>', methods=['POST'])
def delete_city(id):
    brewery_repo.delete_by_id(int(id))
    return redirect('/breweries')