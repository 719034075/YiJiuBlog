from uuid import uuid1

from extensions import db


class Article(db.Model):
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(20))
    catalog = db.Column(db.String(45))
    abstract = db.Column(db.String(255))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    status = db.Column(db.String(10))

    def __init__(self, title, author, catalog, abstract, content, create_time, update_time, status):
        self.id = str(uuid1()),
        self.title = title,
        self.author = author,
        self.catalog = catalog,
        self.abstract = abstract,
        self.content = content,
        self.create_time = create_time,
        self.update_time = update_time,
        self.status = status

    def __repr__(self):
        return "<Model Article `{}`>".format(self.title)
