

from flask import Flask

from .extensions import db, migrate

# Register models.
from .models import *


app = Flask(__name__)

# TODO: dev, prod.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# TODO: Break out app factory.
db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def test():
    return 'Field Poetics'
