from main import db
from flask import Blueprint
from dotenv import load_dotenv
import os

db_commands = Blueprint("db", __name__)

#create 
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")

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