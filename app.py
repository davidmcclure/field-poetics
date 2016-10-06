

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Text(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String, nullable=False)


@app.route('/')
def test():
    return 'Field Poetics'


if __name__ == '__main__':
    app.run(debug=True)
