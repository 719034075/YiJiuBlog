from user.models import User

user = User.query.filter_by(username='admin').first()

print(user)
