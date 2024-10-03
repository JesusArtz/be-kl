from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

# Decorator to check if the user is logged in with a valid token in headers
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        verify_jwt_in_request()
        return f(*args, **kwargs)
    return decorated_function

