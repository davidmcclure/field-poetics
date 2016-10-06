

from flask import Flask

from .extensions import db, migrate
from .models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def test():
    return 'Field Poetics'
