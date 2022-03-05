from main import ma
from models.menu_items import Menu
from marshmallow_sqlalchemy import auto_field

class MenuSchema(ma.SQLAlchemyAutoSchema):
    item_id = auto_field(dump_only=True)

    class Meta:
        model = Menu
        load_instance=True

item_schema = MenuSchema()
items_schema = MenuSchema(many=True)