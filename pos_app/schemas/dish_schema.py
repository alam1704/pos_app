from main import ma
from models.dish import Dish
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields, exceptions, validate

class DishSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dish
        load_instance=True
    
    dish_id = auto_field(dump_only=True)
    dish_name = auto_field(required=True, validate=validate.Length(min=1))
    dish_cost = auto_field(required=True, validate=validate.Range(0,100))
    dish_description = auto_field(required=True, validate=validate.Length(max=1000))



dish_schema = DishSchema()
dishes_schema = DishSchema(many=True)