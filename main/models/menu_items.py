from main import db

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

    # @property
    # def item_image(self):
    #     return f"An image from {self.item_id}"