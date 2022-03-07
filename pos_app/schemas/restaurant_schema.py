from main import ma 
from models.restaurant import Restaurant
from marshmallow_sqlalchemy import auto_field 
from marshmallow import fields, exceptions, validate
from werkzeug.security import generate_password_hash

class RestaurantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Restaurant
        load_instance = True

    restaurant_id = auto_field(dump_only=True)
    restaurant_name = auto_field(required=True, validate=validate.Length(min=1,max=10))
    restaurant_email = auto_field(required=True, validate=validate.Email())
    restaurant_password = fields.Method(
        required=True, 
        load_only=True, 
        deserialize="load_password"
    )

    def load_password(self, password):
        if len(password)>7:
            return generate_password_hash(password, method='sha256')
        raise exceptions.ValidationError("Password must be at least 8 characters.")



restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)
restaurant_update_schema = RestaurantSchema(partial=True)
