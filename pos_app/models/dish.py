from main import db
from datetime import datetime

#setup table in database and retrieve info from that table
class Dish(db.Model):
    #name of table
    __tablename__ = "dish"

    #attributes specify what columns the table should have
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(80), unique=True, nullable=False)
    dish_cost = db.Column(db.Float, nullable=False)
    dish_description = db.Column(db.String(200), nullable=True)
    # ord_order_id = db.relationship('Order', cascade='all,delete', backref='customer', lazy=True)

    @property
    def dish_image(self):
        return f"dish_images/{self.dish_id}.jpg"

class Order(db.Model):
    '''Order table'''
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=datetime.now)
    order_number = db.Column(db.Integer, default=datetime.now().strftime("%f"))
    # dis_dish_id = db.Column(db.Integer, db.ForeignKey('restaurant.restaurant_id'))

    # def __repr__(self):
    #     return f'<OrderID: {self.order_id}>'