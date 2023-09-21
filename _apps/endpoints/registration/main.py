from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, logout_user, login_user, current_user, UserMixin
from flask_bcrypt import Bcrypt
from flask import Blueprint
from flask_migrate import Migrate
from flask_mail import Mail, Message

from .decorators import admin_required, moderator_required, verify_access_token
from decouple import config
from datetime import datetime, timedelta

import uuid
import jwt


SECRET_KEY = config("SECRET_KEY")
MAIL_USERNAME = config('MAIL_USERNAME')
MAIL_PASSWORD = config('MAIL_PASSWORD')


class RegistrationApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
        self.app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        self.app.config['MAIL_PORT'] = 587
        self.app.config['MAIL_USERNAME'] = MAIL_USERNAME
        self.app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
        self.app.config['MAIL_USE_TLS'] = True
        self.app.config['MAIL_USE_SSL'] = False
        self.app.secret_key = SECRET_KEY

        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)

        self.login_manager = LoginManager(self.app)
        self.login_manager.init_app(self.app)
        self.bcrypt = Bcrypt(self.app)
        self.mail = Mail(self.app)
        self.registration = Blueprint('registration', __name__)

        self.register_blueprints()
        self.register_routes()

    def register_blueprints(self):
        self.app.register_blueprint(self.registration)

    def register_routes(self):
        @self.app.route('/')
        def main():
            return '<h1>Main page</h1>'

        @self.login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        @self.app.route('/auth/login', methods=['POST'])
        @self.app.route('/auth/login/', methods=['POST'])
        def login():
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            user = User.query.filter_by(email=email).first()

            if user and self.bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return jsonify({'message': 'Login successful'}), 200
            else:
                return jsonify({'message': 'Invalid email or password'}), 401

        @self.app.route('/auth/logout', methods=['POST'])
        @self.app.route('/auth/logout/', methods=['POST'])
        @login_required
        def logout():
            logout_user()
            return jsonify({'message': 'Logout successful'}), 200

        @self.app.route('/auth/users', methods=['POST'])
        @self.app.route('/auth/users/', methods=['POST'])
        def register():
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            role = data.get('role')

            # Check if the email is already registered
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return jsonify({'message': 'Email already registered'}), 400

            # Hash the password
            hashed_password = self.bcrypt.generate_password_hash(password).decode('utf-8')

            uid = str(uuid.uuid4())

            new_user = User(email=email, password=hashed_password, role=role)
            self.db.session.add(new_user)
            self.db.session.commit()

            payload = {
                'id': new_user.id,
                'email': email,
                'role': role,
                'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration time
            }

            # Generate the JWT token
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            activation_entry = UserActivation(user_id=new_user.id, uid=uid, token=token, activated=False)
            self.db.session.add(activation_entry)
            self.db.session.commit()

            response_data = {
                'email': new_user.email,
                'id': new_user.id,
            }

            return jsonify(response_data), 201

        @self.app.route('/auth/users/activation', methods=['POST'])
        @self.app.route('/auth/users/activation/', methods=['POST'])
        def activate_user():
            data = request.get_json()
            uid = data.get('uid')
            token = data.get('token')

            # Check if the provided UID and token match an entry in the UserActivation table
            activation_entry = UserActivation.query.filter_by(uid=uid, token=token, activated=False).first()

            user = User.query.get(activation_entry.user_id)

            if activation_entry.activated:
                return jsonify({'message': f'На email {user.email} отправлено письмо.'
                                           f' Перейдите по ссылке в письме для подтверждения Вашего email.'}), 200

            user.role = 'active'

            send_activation_email(user.email)

            activation_entry.activated = True
            self.db.session.commit()

            response_data = {
                'uid': uid,
                'token': token
            }

            return jsonify(response_data), 200


        @self.app.route('/auth/users/reset_password/<token>', methods=['POST'])
        @self.app.route('/auth/users/reset_password/<token>/', methods=['POST'])
        @login_required
        def reset_password(token):
            data = request.get_json()
            password = data.get('password')

            reset_entry = PasswordReset.query.filter_by(token=token).first()

            if not reset_entry:
                return jsonify({'message': 'Invalid reset token'}), 400

            user = User.query.get(reset_entry.user_id)
            user.password = self.bcrypt.generate_password_hash(password).decode('utf-8')

            self.db.session.delete(reset_entry)
            self.db.session.commit()

            return jsonify({'message': 'Password reset successful.'}), 200

        @self.app.route('/auth/users/reset_password', methods=['POST'])
        @self.app.route('/auth/users/reset_password/', methods=['POST'])
        @login_required
        def request_reset_password():
            data = request.get_json()
            email = data.get('email')

            user = User.query.filter_by(email=email).first()

            if not user:
                return jsonify({'message': 'Посмотрите вашу почту'}), 200

            payload = {
                'email': user.email,
                'exp': datetime.utcnow() + timedelta(hours=1)
            }

            reset_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            # Store a unique token in the database
            password_reset_entry = PasswordReset(user_id=user.id, token=reset_token)
            self.db.session.add(password_reset_entry)
            self.db.session.commit()

            # Send an email with a link containing the reset_token
            send_password_reset_email(email, reset_token)

            return jsonify({'message': 'Посмотрите вашу почту'}), 200

        @self.app.route('/auth/users/me')
        @self.app.route('/auth/users/me/')
        @verify_access_token
        def get_user_info(user_info):
            return jsonify(user_info)

        @self.app.route('/auth/users/set_email', methods=['POST'])
        @self.app.route('/auth/users/set_email/', methods=['POST'])
        @login_required
        def set_new_email():
            data = request.get_json()

            if data is None:
                return jsonify({'message': 'Invalid request data'}), 400

            current_password = data.get('password')
            new_email = data.get('new_email')

            if not current_user.is_authenticated:
                return jsonify({'message': 'User is not logged in'}), 401

            if not self.bcrypt.check_password_hash(current_user.password, current_password):
                return jsonify({'message': 'Incorrect current password'}), 400

            existing_user = User.query.filter_by(email=new_email).first()
            if existing_user:
                return jsonify({'message': 'Email already registered'}), 400

            current_user.new_email = new_email
            self.db.session.commit()

            return jsonify({'current_password': current_password, 'new_email': new_email}), 200

        def send_activation_email(email):
            message = Message('Account Activation', sender=self.app.config['MAIL_USERNAME'], recipients=[email])
            message.body = 'Ваш аккаунт активирован! Спасибо за регистрацию!'
            self.mail.send(message)

        def send_password_reset_email(email, reset_token):
            reset_link = f"https://test.itcoty.ru/auth/users/reset_password/{reset_token}"
            message = Message('Восстановление пароля', sender=self.app.config['MAIL_USERNAME'], recipients=[email])
            message.html = render_template('password_reset_email.html', reset_link=reset_link)
            self.mail.send(message)

    def run(self):
        with self.app.app_context():
            self.db.create_all()
            print('Database created')

        self.app.run(debug=True)


registration_app = RegistrationApp()


class User(registration_app.db.Model, UserMixin):
    id = registration_app.db.Column(registration_app.db.Integer, primary_key=True)
    email = registration_app.db.Column(registration_app.db.String(120), unique=True, nullable=False)
    password = registration_app.db.Column(registration_app.db.String(60), nullable=False)
    role = registration_app.db.Column(registration_app.db.String(20), default='user')
    new_email = registration_app.db.Column(registration_app.db.String(120), unique=True)


class UserActivation(registration_app.db.Model):
    id = registration_app.db.Column(registration_app.db.Integer, primary_key=True)
    user_id = registration_app.db.Column(registration_app.db.Integer, registration_app.db.ForeignKey('user.id'), nullable=False)
    uid = registration_app.db.Column(registration_app.db.String(120), nullable=False)
    token = registration_app.db.Column(registration_app.db.String(120), nullable=False)
    activated = registration_app.db.Column(registration_app.db.Boolean, default=False)
    created_at = registration_app.db.Column(registration_app.db.DateTime, default=datetime.utcnow)


class PasswordReset(registration_app.db.Model):
    id = registration_app.db.Column(registration_app.db.Integer, primary_key=True)
    user_id = registration_app.db.Column(registration_app.db.Integer, registration_app.db.ForeignKey('user.id'), nullable=False)
    token = registration_app.db.Column(registration_app.db.String(120), nullable=False)



