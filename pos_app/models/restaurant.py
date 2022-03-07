from main import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Restaurant(UserMixin, db.Model):
    __tablename__ = 'restaurant'
    
    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(100), nullable=False)
    restaurant_email = db.Column(db.String(40), unique=True, nullable=False)
    restaurant_password = db.Column(db.String(200), nullable=False)

    def get_id(self):
        return self.resturant_id

    def check_password(self, password):
        return check_password_hash(self.password, password)