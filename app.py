from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
import os
from models import db, Application, Reference, Employment

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1Cowbirds@localhost:5432/the-growing-place'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


@app.route("/")
def hello():
    return "Hello, World"

