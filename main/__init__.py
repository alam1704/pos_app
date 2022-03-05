from crypt import methods
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# using multiple assignments and list comprehension to import variables
(
    db_user, 
    db_pass, 
    db_name, 
    db_domain
) = (os.environ.get(item) for item in [
    "DB_USER", 
    "DB_PASS", 
    "DB_NAME", 
    "DB_DOMAIN"
    ]
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_domain}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Menu(db.Model):
    __tablename__ = "menu_items"
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), unique=True, nullable=False)
    item_cost = db.Column(db.float)

@app.route('/menu_items/', methods=['GET'])
def menu_retrieve():
    #Will retrieve an entire menu/the home page
    return "Retrieve menu"

@app.route('/menu_calculator/')
def calculator_index():
    # Will return a calculator index page
    return "renders a calculator"

@app.route('/cart/', methods=['GET'])
def cart():
    #will return page/side-page of cart
    return "renders page for cart"

@app.route('/addToCart/', methods=['PUT', 'PATCH'])
def addToCart():
    # will prompt user to enter qty then add qty and item to cart
    return "Will return item into cart"

@app.route('/menu_items/<int:id>/', methods=['GET'])
def item_retrieve():
    # Will retrieve a specific item on the menu
    return f'Retrieve {id} Item'

@app.route('/menu_items/<int:id>/', methods=['POST'])
def item_create():
    # Will create a specific new item on the menu
    return f"Create {id} item"

@app.route('/menu_items/<int:id>/', methods=['PUT', 'PATCH'])
def item_update():
    # Will update specific item on the menu
    return f"Update {id} item"

@app.route('/menu_items/<int:id>/', methods=['DELETE'])
def item_delete():
    # Will delete specific item on menu
    return f"Delete {id} Item"


if __name__ == '__main__':
    app.run(debug=True) 