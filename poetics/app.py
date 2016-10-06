

from flask import Flask
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from .extensions import db, migrate, admin
from .models import Text


app = Flask(__name__)

app.secret_key = 'dev'

# TODO: dev, prod.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/poetics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TODO: Break out app factory.

admin = Admin(template_mode='bootstrap3')
admin.add_view(ModelView(Text, db.session))

db.init_app(app)
migrate.init_app(app, db)
admin.init_app(app)


@app.route('/')
def test():
    return 'Field Poetics'
