from functools import wraps
from flask import jsonify, redirect, url_for
from flask_login import current_user


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