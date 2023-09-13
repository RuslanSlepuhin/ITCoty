from functools import wraps
from flask import jsonify, request
from flask_login import current_user

from decouple import config

import jwt
import secrets


def admin_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'administrator':
            return jsonify({'message': 'Access denied. Administrator role required'}), 403
        return f(*args, **kwargs)
    return decorated_func


def moderator_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'moderator':
            return jsonify({'message': 'Access denied. Moderator role required'}), 403
        return f(*args, **kwargs)
    return decorated_func


def verify_access_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access_token = request.headers.get('Authorization')

        if not access_token:
            return jsonify({'message': 'Access token is missing'}), 401

        try:
            token = access_token.split()[1]
            decoded_token = jwt.decode(token, config('SECRET_KEY'), algorithms=['HS256'])

            user_info = {
                'id': decoded_token['id'],
                'email': decoded_token['email']
            }

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401

        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return func(user_info, *args, **kwargs)

    return wrapper
