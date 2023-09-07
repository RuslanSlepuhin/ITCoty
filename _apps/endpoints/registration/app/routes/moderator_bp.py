from flask import Blueprint
from flask_login import login_required, current_user
from _apps.endpoints.registration.models import User
from _apps.endpoints.registration.app.decorators import moderator_required


moderator_blueprint = Blueprint('moderator', __name__, url_prefix='/moderator')


@moderator_blueprint.route('/manage')
@login_required
@moderator_required
def manage_moderators():
    moderators = User.query.filter_by(role='moderator').all()