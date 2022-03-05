from main import ma
from models.menu_items import Menu
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields, exceptions, validate

class MenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Menu
        load_instance=True
    
    item_id = auto_field(dump_only=True)
    item_name = auto_field(required=True, validate=validate.Length(min=1))
    item_cost = auto_field(required=True, validate=validate.Range(0,100))
    item_description = auto_field(required=True, validate=validate.Length(max=1000))



item_schema = MenuSchema()
items_schema = MenuSchema(many=True)