from flask import Blueprint, request, render_template, redirect, url_for, abort, flash
from main import db, lm
from models.restaurant import Restaurant
from schemas.restaurant_schema import restaurants_schema, restaurant_schema, restaurant_update_schema
from flask_login import login_user, logout_user, login_required, current_user
from marshmallow import ValidationError

@lm.user_loader
def load_manager(restaurant):
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

@restaurant.route("/signup/", methods=['GET', 'POST'])
def sign_up():
    data = {
        "page_title":"Restaurant Sign Up"
    }
    if request.method == "GET":
        return render_template("restaurant_signup.html", page_data=data)
    try:
        new_restaurant = restaurant_schema.load(request.form)
        db.session.add(new_restaurant)
        db.session.commit()
        login_user(new_restaurant)
        return redirect(url_for("restaurant.restaurant_detail"))
    except Exception as error:
        return "Username or Email already exists, please go back and try again."


@restaurant.route("/login/", methods=['GET', 'POST'])
def log_in():
    data = {
        "page_title":"Welcome!"
    }
    if request.method == "GET":
        return render_template("restaurant_login.html", page_data=data)
    
    restaurant = Restaurant.query.filter_by(restaurant_email=request.form["restaurant_email"]).first()
    if restaurant and restaurant.check_password(password=request.form["restaurant_password"]):
        login_user(restaurant)
        return redirect(url_for("restaurant.restaurant_detail"))

    abort(401, "Login Unsuccessful. Did you supply the correct username and password?")

#see if we can add URL_mapping for current user i.e. /<username>/account/
@restaurant.route("/account/", methods=['GET','POST'])
@login_required
def restaurant_detail():
    if request.method=="GET":
        data = {"page_title":"Account details"}
        return render_template("restaurant_detail.html", page_data=data)
    else:
        restaurant=Restaurant.query.filter_by(restaurant_id=current_user.restaurant_id)
        updated_fields=restaurant_schema.dump(request.form)
        errors = restaurant_update_schema.validate(updated_fields)

    if errors:
        raise ValidationError(message=errors)
    else:
        restaurant.update(updated_fields)
        db.session.commit()
        return redirect(url_for("restaurant.restaurant_detail"))

@restaurant.route("/logout/", methods=["POST"])
@login_required
def log_out():
    logout_user()
    return redirect(url_for("restaurant.log_in"))