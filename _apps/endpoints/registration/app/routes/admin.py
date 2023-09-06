from flask import Blueprint
from flask_login import login_required, current_user
from _apps.endpoints.registration.models import User
from .decorators import admin_required


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()