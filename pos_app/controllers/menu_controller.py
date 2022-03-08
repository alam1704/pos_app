from flask import Blueprint, jsonify, request, render_template
from main import db
from models.menu_items import Menu
from schemas.menu_schema import item_schema, items_schema
from flask_login import login_user, logout_user, login_required, current_user

# create menu_items controller
menu_items = Blueprint('menu_items', __name__)

@menu_items.route('/')
@login_required
def calculator_index():
    # Will return a calculator index page
    data={
        "page_title":"Manual Entry"
    }
    return render_template("calculator.html", page_data=data)

@menu_items.route('/cart/', methods=['GET'])
@login_required
def cart():
    #will return page/side-page of cart
    return "renders page for cart"

@menu_items.route('/addToCart/', methods=['PUT', 'PATCH'])
@login_required
def add_item_to_cart():
    # will prompt user to enter qty then add qty and item to cart
    return "Will return item into cart"

@menu_items.route('/menu_items/', methods=['GET'])
@login_required
def menu_retrieve():
    #Will retrieve an entire menu/the home page
    menu_items=Menu.query.all()
    data = {
        "page_title": "Menu",
        "menu_items": items_schema.dump(menu_items)
    }
    return render_template("item_menu.html", page_data=data)

@menu_items.route('/menu_items/<int:id>/', methods=['GET'])
@login_required
def item_retrieve(id):
    # Will retrieve a specific item on the menu
    menu_item=Menu.query.get_or_404(id)
    data = {
        "page_title":"Item Details",
        "menu_items": item_schema.dump(menu_item)
    }
    return render_template("item_detail.html", page_data=data)

@menu_items.route('/menu_items/<int:id>/', methods=['PUT', 'PATCH'])
@login_required
def item_update(id):
    # Will update specific item on the menu
    menu_item=Menu.query.filter_by(item_id=id)
    updated_fields=item_schema.dump(request.json)
    if updated_fields:
        menu_item.update(updated_fields) # how to update multiple fields of an item
        db.session.commit()
    return jsonify(item_schema.dump(menu_item.first()))

@menu_items.route('/menu_items/<int:id>/', methods=['DELETE'])
@login_required
def item_delete(id):
    # Will delete specific item on menu
    menu_item=Menu.query.get_or_404(id)
    db.session.delete(menu_item)
    db.session.commit()
    return jsonify(item_schema.dump(menu_item))

@menu_items.route('/new_item/', methods=['GET'])
@login_required
def new_item_index():
    data={
        "page_title":"Add New Item"
    }
    return render_template("item_new.html", page_data=data)

@menu_items.route('/new_item/', methods=['POST'])
@login_required
def item_create():
    # Will create a specific new item on the menu
    new_item=item_schema.load(request.form) #how do i add multiple fields to add to the menu item
    db.session.add(new_item)
    db.session.commit()
    return jsonify(item_schema.dump(new_item))