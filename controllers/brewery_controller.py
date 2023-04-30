from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.brewery import Brewery
import repositories.brewery_repository as brewery_repo

brewery_blueprint = Blueprint("brewery", __name__)

brewery_blueprint.route("/brewery")
def locations():
    locations = brewery_repo.select_all() 
    return render_template("brewery/index.jinja", brewery = Brewery)

@brewery_blueprint.route("/brewery/<id>")
def show(id):
    brewery = brewery_repo.select(id)
    return render_template("brewery/show.", brewery = Brewery)
