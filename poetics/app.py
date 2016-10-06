

from flask import Flask
from flask_migrate import Migrate

from .database import db
from .models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def test():
    return 'Field Poetics'