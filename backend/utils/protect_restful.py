from functools import wraps
from flask_jwt_extended import get_jwt_identity
from .response_bean import ResponseBean
from user.models import User


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            jwt_user = get_jwt_identity()
            current_user = User.query.filter_by(username=jwt_user).first()
            if current_user.roles not in roles:
                response = ResponseBean().get_fail_instance()
                response.message = '非法用戶'
                return response.__dict__
            return f(*args, **kwargs)

        return wrapped

    return wrapper
