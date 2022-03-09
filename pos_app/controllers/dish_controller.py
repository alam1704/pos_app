from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from main import db
from models.dish import Dish
from models.dish import Order
from schemas.dish_schema import dish_schema, dishes_schema
from schemas.order_schema import order_schema, orders_schema
from flask_login import login_user, logout_user, login_required, current_user

# create dishes controller
dishes = Blueprint('dishes', __name__)

@dishes.route('/numpad/')
@login_required
def numpad():
    # Will return a calculator index page
    data={
        "page_title":"Manual Entry"
    }
    return render_template("numpad.html", page_data=data)

@dishes.route('/cart/', methods=['GET'])
@login_required
def cart():
    #will return page/side-page of cart
    return "renders page for cart"

@dishes.route('/addToCart/<int:id>')
@login_required
def add_dish_to_cart(id):
    # will prompt user to enter qty then add qty and item to cart

    return "Will return item into cart"

@dishes.route('/dishes/', methods=['GET'])
@login_required
def menu_retrieve():
    #Will retrieve an entire menu/the home page
    dishes=Dish.query.all()
    data = {
        "page_title": "Menu",
        "dishes": dishes_schema.dump(dishes)
    }
    return render_template("dish_menu.html", page_data=data)

@dishes.route('/dishes/<int:id>/', methods=['GET'])
@login_required
def item_retrieve(id):
    # Will retrieve a specific item on the menu
    dish=Dish.query.get_or_404(id)
    data = {
        "page_title":"Dish Details",
        "dish": dish_schema.dump(dish)
    }
    return render_template("dish_detail.html", page_data=data)

@dishes.route('/dishes/<int:id>/', methods=["POST"])
@login_required
def item_update(id):
    # Will update specific item on the menu
    dish=Dish.query.filter_by(dish_id=id)
    updated_fields=dish_schema.dump(request.form)
    if updated_fields:
        dish.update(updated_fields) # how to update multiple fields of an item
        db.session.commit()
    data={
        "page_title":"Dish Details",
        "dish": dish_schema.dump(dish.first())
    }
    return render_template("dish_detail.html", page_data=data)

@dishes.route('/dishes/<int:id>/delete/', methods=['POST'])
@login_required
def item_delete(id):
    # Will delete specific item on menu
    dish=Dish.query.get_or_404(id)
    db.session.delete(dish)
    db.session.commit()
    return redirect(url_for("dishes.menu_retrieve"))

@dishes.route('/new_item/', methods=['GET'])
@login_required
def new_item_index():
    data={
        "page_title":"Add New Item"
    }
    return render_template("item_new.html", page_data=data)

@dishes.route('/new_item/', methods=['POST'])
@login_required
def item_create():
    # Will create a specific new item on the menu
    new_item=dish_schema.load(request.form) #how do i add multiple fields to add to the menu item
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for("dishes.menu_retrieve"))