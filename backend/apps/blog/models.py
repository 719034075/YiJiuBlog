from uuid import uuid1

from extensions import db


class Blog(db.Model):
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    context = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __init__(self, title, author, context, create_time, update_time):
        self.id = str(uuid1()),
        self.title = title,
        self.author = author,
        self.context = context,
        self.create_time = create_time,
        self.update_time = update_time

    def __repr__(self):
        return "<Model Blog `{}`>".format(self.title)


