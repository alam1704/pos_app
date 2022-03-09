from main import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Restaurant(UserMixin, db.Model):
    __tablename__ = 'restaurant'
    
    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(25), nullable=False)
    restaurant_email = db.Column(db.String(100), unique=True, nullable=False)
    restaurant_password = db.Column(db.String(200), nullable=False)
    ord_order_id = db.relationship('Order', cascade='all,delete', backref='customer', lazy=True)

    # def __init__ (self, restaurant_name, restaurant_email)
    #     self.restaurant_name=restaurant_name
    #     self.restaurant_email=restaurant_email

    # def __repr__(self):
    #     return f'<Restaurant: {self.restaurant_id} {self.restaurant_name}>'

    def get_id(self):
        return self.restaurant_id

    def check_password(self, password):
        return check_password_hash(self.restaurant_password, password)

class Order(db.Model):
    '''Order table'''
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=datetime.now)
    order_number = db.Column(db.Integer, default=datetime.now().strftime("%f"))
    res_restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.restaurant_id'))

    # def __repr__(self):
    #     return f'<OrderID: {self.order_id}>'