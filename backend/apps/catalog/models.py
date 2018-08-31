from uuid import uuid1

from extensions import db


class Catalog(db.Model):
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    amount = db.Column(db.Integer)

    def __init__(self, name):
        self.id = str(uuid1()),
        self.name = name,
        self.amount = 0

    def __repr__(self):
        return "<Model Catalog `{}`>".format(self.name)
