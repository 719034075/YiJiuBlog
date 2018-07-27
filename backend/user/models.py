from uuid import uuid1

from extensions import db, bcrypt


class User(db.Model):
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    avatar = db.Column(db.String(255))
    roles = db.Column(db.String(80))

    def __init__(self, username, password, roles):
        self.id = str(uuid1()),
        self.username = username,
        self.password = self.set_password(password),
        self.roles = roles

    def __repr__(self):
        return "<Model User `{}`>".format(self.username)

    def set_password(self, password):
        return bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
