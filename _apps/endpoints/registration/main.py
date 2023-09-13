from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, logout_user, login_user, current_user, UserMixin
from flask_bcrypt import Bcrypt
from flask import Blueprint
from flask_migrate import Migrate
from flask_mail import Mail, Message

from decorators import admin_required, moderator_required, verify_access_token
from decouple import config
from datetime import datetime, timedelta

import uuid
import jwt


SECRET_KEY = config("SECRET_KEY")

MAIL_USERNAME = config('MAIL_USERNAME')
MAIL_PASSWORD = config('MAIL_PASSWORD')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

app.secret_key = SECRET_KEY


db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.init_app(app)

bcrypt = Bcrypt(app)

mail = Mail(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), default='user')
    new_email = db.Column(db.String(120), unique=True)


class UserActivation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uid = db.Column(db.String(120), nullable=False)
    token = db.Column(db.String(120), nullable=False)
    activated = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class PasswordReset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(120), nullable=False)


# Create the main blueprint
registration = Blueprint('registration', __name__)


@app.route('/')
def main():
    return '<h1>Main page</h1>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@registration.route('/auth/login', methods=['POST'])
@registration.route('/auth/login/', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401


@registration.route('/auth/logout', methods=['POST'])
@registration.route('/auth/logout/', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'Logout successful'}), 200

    return jsonify({'message': 'You are not logged in'}), 401


@registration.route('/auth/users', methods=['POST'])
@registration.route('/auth/users/', methods=['POST'])
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
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    uid = str(uuid.uuid4())

    new_user = User(email=email, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    payload = {
        'id': new_user.id,
        'email': email,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration time
    }

    # Generate the JWT token
    token = jwt.encode(payload, config('SECRET_KEY'), algorithm='HS256')

    activation_entry = UserActivation(user_id=new_user.id, uid=uid, token=token, activated=False)
    db.session.add(activation_entry)
    db.session.commit()

    response_data = {
        'email': new_user.email,
        'id': new_user.id,
    }

    return jsonify(response_data), 201


@registration.route('/auth/users/activation', methods=['POST'])
@registration.route('/auth/users/activation/', methods=['POST'])
def activate_user():
    data = request.get_json()
    uid = data.get('uid')
    token = data.get('token')

    # Check if the provided UID and token match an entry in the UserActivation table
    activation_entry = UserActivation.query.filter_by(uid=uid, token=token, activated=False).first()

    user = User.query.get(activation_entry.user_id)

    if activation_entry.activated:
        return jsonify({'message': f'На email {user.email} отправлено письмо. Перейдите по ссылке в письме для подтверждения Вашего email.'}), 200

    user.role = 'active'

    send_activation_email(user.email)

    activation_entry.activated = True
    db.session.commit()

    response_data = {
        'uid': uid,
        'token': token
    }

    return jsonify(response_data), 200


@login_required
@app.route('/auth/users/reset_password', methods=['POST'])
@app.route('/auth/users/reset_password/', methods=['POST'])
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

    reset_token = jwt.encode(payload, config('SECRET_KEY'), algorithm='HS256')

    # Store a unique token in the database
    password_reset_entry = PasswordReset(user_id=user.id, token=reset_token)
    db.session.add(password_reset_entry)
    db.session.commit()

    # Send an email with a link containing the reset_token
    send_password_reset_email(email, reset_token)

    return jsonify({'message': 'Посмотрите вашу почту'}), 200


@login_required
@app.route('/auth/users/reset_password/<token>', methods=['POST'])
@app.route('/auth/users/reset_password/<token>/', methods=['POST'])
def reset_password(token):
    data = request.get_json()
    password = data.get('password')

    reset_entry = PasswordReset.query.filter_by(token=token).first()

    if not reset_entry:
        return jsonify({'message': 'Invalid reset token'}), 400

    user = User.query.get(reset_entry.user_id)
    user.password = bcrypt.generate_password_hash(password).decode('utf-8')

    db.session.delete(reset_entry)
    db.session.commit()

    return jsonify({'message': 'Password reset successful.'}), 200


@app.route('/auth/users/me')
@app.route('/auth/users/me/')
@verify_access_token
def get_user_info(user_info):
    return jsonify(user_info)


@login_required
@app.route('/auth/users/set_email', methods=['POST'])
@app.route('/auth/users/set_email/', methods=['POST'])
def set_email():
    data = request.get_json()

    if data is None:
        return jsonify({'message': 'Invalid request data'}), 400

    current_password = data.get('password')
    new_email = data.get('new_email')

    if not current_user.is_authenticated:
        return jsonify({'message': 'User is not logged in'}), 401

    if not bcrypt.check_password_hash(current_user.password, current_password):
        return jsonify({'message': 'Incorrect current password'}), 400

    existing_user = User.query.filter_by(email=new_email).first()
    if existing_user:
        return jsonify({'message': 'Email already registered'}), 400

    current_user.new_email = new_email
    db.session.commit()

    return jsonify({'current_password': current_password, 'new_email': new_email}), 200


def send_activation_email(email):
    message = Message('Account Activation', sender=app.config['MAIL_USERNAME'], recipients=[email])
    message.body = 'Ваш аккаунт активирован! Спасибо за регистрацию!'
    mail.send(message)


def send_password_reset_email(email, reset_token):
    reset_link = f"https://test.itcoty.ru/auth/users/reset_password/{reset_token}"
    message = Message('Восстановление пароля', sender=app.config['MAIL_USERNAME'], recipients=[email])
    message.html = render_template('password_reset_email.html', reset_link=reset_link)
    mail.send(message)


app.register_blueprint(registration)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print('Database created')

    app.run(debug=True)
