from uuid import uuid1

from extensions import db


class Blog(db.Model):
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    abstract = db.Column(db.String(255))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __init__(self, title, abstract, content, create_time, update_time):
        self.id = str(uuid1()),
        self.title = title,
        self.abstract = abstract,
        self.content = content,
        self.create_time = create_time,
        self.update_time = update_time

    def __repr__(self):
        return "<Model Blog `{}`>".format(self.title)
