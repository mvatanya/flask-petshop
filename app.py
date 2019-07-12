"""Flask application for a pet store: can view and add pets."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from db import Pet

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

toolbar = DebugToolbarExtension(app)

@app.route('/')
def getPets():
    all_pets = Pet.get_all()
    return render_template("home.html",pet_list=all_pets)

@app.route('/pets/add-pet')
def addPets():
    return render_template("add-pet-form.html")

@app.route('/pets/add-pet', methods = ["POST"])
def post_pet():
    name = request.form["name"]
    age = request.form["age"]
    color = request.form["color"]
    photo = request.form["photo"]
    flash("Pet added!")
    return redirect ("/")

@app.route('/pets/<id_of_pet>')
def show_pet(id_of_pet):
    pet = Pet.find_by_id(id_of_pet)
    return render_template("show_pet.html", pet=pet )