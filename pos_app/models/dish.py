from main import db

#setup table in database and retrieve info from that table
class Dish(db.Model):
    #name of table
    __tablename__ = "dish"

    #attributes specify what columns the table should have
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(80), unique=True, nullable=False)
    dish_cost = db.Column(db.Float, nullable=False)
    dish_description = db.Column(db.String(200), nullable=True)

    # @property
    # def item_image(self):
    #     return f"An image from {self.item_id}"