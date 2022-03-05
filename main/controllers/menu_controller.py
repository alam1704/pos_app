from flask import Blueprint, jsonify, request
from main import db
from models.menu_items import Menu
from schemas.menu_schema import item_schema, items_schema

# create menu_items controller
menu_items = Blueprint('menu_items', __name__)

@menu_items.route('/menu_items/', methods=['GET'])
def menu_retrieve():
    #Will retrieve an entire menu/the home page
    menu_items=Menu.query.all()
    return jsonify(items_schema.dump(menu_items))

@menu_items.route('/menu_calculator/')
def calculator_index():
    # Will return a calculator index page
    return "renders a calculator"

@menu_items.route('/cart/', methods=['GET'])
def cart():
    #will return page/side-page of cart
    return "renders page for cart"

@menu_items.route('/addToCart/', methods=['PUT', 'PATCH'])
def addToCart():
    # will prompt user to enter qty then add qty and item to cart
    return "Will return item into cart"

@menu_items.route('/menu_items/<int:id>/', methods=['GET'])
def item_retrieve(id):
    # Will retrieve a specific item on the menu
    menu_item=Menu.query.get_or_404(id)
    return jsonify(item_schema.dump(menu_item))

@menu_items.route('/menu_items/', methods=['POST'])
def item_create():
    # Will create a specific new item on the menu
    new_item= item_schema.load(request.json) #how do i add multiple fields to add to the menu item
    db.session.add(new_item)
    db.session.commit()
    return jsonify(item_schema.dump(new_item))

@menu_items.route('/menu_items/<int:id>/', methods=['PUT', 'PATCH'])
def item_update(id):
    # Will update specific item on the menu
    menu_item=Menu.query.filter_by(item_id=id)
    updated_fields=item_schema.dump(request.json)
    if updated_fields:
        menu_item.update(updated_fields) # how to update multiple fields of an item
        db.session.commit()
    return jsonify(item_schema.dump(menu_item.first()))

@menu_items.route('/menu_items/<int:id>/', methods=['DELETE'])
def item_delete(id):
    # Will delete specific item on menu
    menu_item=Menu.query.get_or_404(id)
    db.session.delete(menu_item)
    db.session.commit()
    return jsonify(item_schema.dump(menu_item))