from flask import Blueprint, request, render_template, redirect, url_for, abort, flash
from main import db, lm
from models.restaurant import Restaurant
from schemas.restaurant_schema import restaurants_schema, restaurant_schema, restaurant_update_schema
from flask_login import login_user, logout_user, login_required, current_user
from marshmallow import ValidationError

@lm.user_loader
def load_staff(restaurant):
    return Restaurant.query.get(restaurant)

@lm.unauthorized_handler
def unauthorized():
    return redirect('/restaurant/login/')

#does the blueprint use the tablename from models?
restaurant = Blueprint('restaurant', __name__)

@restaurant.route("/restaurant/", methods=['GET'])
def retrieve_restaurants():
    restaurant_list=Restaurant.query.all()
    data = {
        "page_title":"Restaurant Index",
        "Restaurant":restaurants_schema.dump(restaurant_list)
    } 
    return render_template("restaurant_index.html", page_data=data)

@restaurant.route("/restaurant/", methods=['GET', 'POST'])
def sign_up():
    data = {
        "page_title":"Restaurant Sign Up"
    }
    if request.method == "GET":
        return render_template("restaurant_signup.html", page_data=data)

    new_restaurant = restaurant_schema.load(request.form)
    db.session.add(new_restaurant)
    db.session.commit()
    login_user(new_restaurant)
    return redirect(url_for("restaurant.retrieve_restaurants"))