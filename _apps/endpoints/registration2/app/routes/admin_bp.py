from flask import Blueprint
from flask_login import login_required, current_user
from _apps.endpoints.registration.models import User
from _apps.endpoints.registration.app.decorators import admin_required


admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blueprint.route('/dashboard')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.filter_by(role='administrator').all()
