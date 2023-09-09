from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'registration2', 'users.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from _apps.endpoints.registration.models import User, UserActivation, PasswordReset

with app.app_context():
    db.create_all()
    print('DataBase created')


from _apps.endpoints.registration.app import views
from _apps.endpoints.registration.app import registration

from _apps.endpoints.registration.app.routes.admin_bp import admin_blueprint
from _apps.endpoints.registration.app.routes.moderator_bp import moderator_blueprint

app.register_blueprint(admin_blueprint)
app.register_blueprint(moderator_blueprint)

