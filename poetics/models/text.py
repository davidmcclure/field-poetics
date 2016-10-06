

from poetics.extensions import db


class Text(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String, nullable=False)

    markup = db.Column(db.String, nullable=False)
