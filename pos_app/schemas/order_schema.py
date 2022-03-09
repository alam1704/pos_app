from main import ma
from models.dish import Dish, Order
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields, exceptions, validate

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance=True
    
    order_id = auto_field(dump_only=True)
    
    



order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)