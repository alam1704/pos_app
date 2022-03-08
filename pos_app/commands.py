from main import db
from flask import Blueprint
from dotenv import load_dotenv
import os

db_commands = Blueprint("db-custom", __name__)

#create 
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF exists alembic_version;")
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.menu_items import Menu
    from faker import Faker
    faker=Faker()

    for i in range(5):
        menu_item=Menu(
            item_name=faker.name(), 
            item_cost=float(faker.random_number()), 
            item_description=faker.catch_phrase())
        db.session.add(menu_item)

    db.session.commit()
    print("Tables seeded")

@db_commands.cli.command("export")
def export_db():
    "Exports all data from the database into a text document"
    load_dotenv()
    user = os.environ.get('DB_USER') 
    password = os.environ.get('DB_PASS') 
    database = os.environ.get('DB_NAME') 
    domain = os.environ.get('DB_DOMAIN')
    os.system(f"pg_dump --dbname=postgresql://{user}:{password}@{domain}/{database} -f dump.txt")  
    print("Data backed up to dump.txt")

@db_commands.cli.command("reset")
def reset_db():
    """Drops, creates, and seeds tables in one step."""
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted!")
    db.create_all()
    print("Tables created!")
    from models.menu_items import Menu
    from faker import Faker
    faker = Faker()

    for i in range(10):
        menu_item=Menu(
            item_name=faker.name(), 
            item_cost=float(faker.random_number()), 
            item_description=faker.catch_phrase())
        db.session.add(menu_item)
    
    db.session.commit()
    print("Tables seeded!")