from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

def create_app():

    # creating a flask app object
    app = Flask(__name__)

    # configure the app
    app.config.from_object("config.app_config")

    #creating database object for our Object relational mapper
    db = SQLAlchemy(app)


    #setup table in database and retrieve info from that table
    class Menu(db.Model):
        #name of table
        __tablename__ = "menu_items"

        #attributes specify what columns the table should have
        item_id = db.Column(db.Integer, primary_key=True)
        item_name = db.Column(db.String(80), unique=True, nullable=False)
        item_cost = db.Column(db.Float, nullable=False)
        item_description = db.Column(db.String(200), nullable=True)

        #creates python object that will allows new row creation
        def __init__(self, item_name, item_cost, item_description):
            self.item_name=item_name
            self.item_cost=item_cost
            self.item_description=item_description

        #To convert to JSON 
        @property 
        def serialize(self):
            return {
                "item_id":self.item_id,
                "item_name":self.item_name,
                "item_cost":self.item_cost,
                "item_description":self.item_description
            }

    #creates database tables when app starts
    db.create_all()

        # @property
        # def item_image(self):
        #     return f"An image from {self.item_id}"

    @app.route('/menu_items/', methods=['GET'])
    def menu_retrieve():
        #Will retrieve an entire menu/the home page
        menu_items=Menu.query.all()
        return jsonify([menu_item.serialize for menu_item in menu_items])

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
    def item_retrieve(id):
        # Will retrieve a specific item on the menu
        menu_item=Menu.query.get_or_404(id)
        return jsonify(menu_item.serialize)

    @app.route('/menu_items/<int:id>/', methods=['POST'])
    def item_create():
        # Will create a specific new item on the menu
        new_item= Menu(request.json['item_name']) #how do i add multiple fields to add to the menu item
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.serialize)

    @app.route('/menu_items/<int:id>/', methods=['PUT', 'PATCH'])
    def item_update(id):
        # Will update specific item on the menu
        menu_item=Menu.query.filter_by(item_id=id)
        menu_item.update(dict(item_name=request.json["item_name"])) # how to update multiple fields of an item
        db.session.commit()
        return jsonify(menu_item.first().serialize)

    @app.route('/menu_items/<int:id>/', methods=['DELETE'])
    def item_delete(id):
        # Will delete specific item on menu
        menu_item=Menu.query.get_or_404(id)
        db.session.delete(menu_item)
        db.session.commit()
        return jsonify(menu_item.serialize)

    return app