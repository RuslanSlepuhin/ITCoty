from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
from flask_bcrypt import Bcrypt
from flask import Blueprint
from flask_migrate import Migrate
from flask_mail import Mail, Message

from decorators import admin_required, moderator_required
from datetime import datetime
from decouple import config

import uuid


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


db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

mail = Mail(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), default='user')


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


@registration.route('/auth/users', methods=['POST'])
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
    token = str(uuid.uuid4())

    new_user = User(email=email, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    activation_entry = UserActivation(user_id=new_user.id, uid=uid, token=token, activated=False)
    db.session.add(activation_entry)
    db.session.commit()

    response_data = {
        'email': new_user.email,
        'id': new_user.id,
        'uid': uid,
        'token': token
    }

    return jsonify(response_data), 201


@registration.route('/auth/users/activation', methods=['POST'])
def activate_user():
    data = request.get_json()
    uid = data.get('uid')
    token = data.get('token')

    # Check if the provided UID and token match an entry in the UserActivation table
    activation_entry = UserActivation.query.filter_by(uid=uid, token=token, activated=False).first()

    if not activation_entry:
        return jsonify({'message': 'Invalid activation data'}), 400

    user = User.query.get(activation_entry.user_id)

    if activation_entry.activated:
        return jsonify({'message': 'User already activated'}), 200

    user.role = 'active'

    send_activation_email(user.email)

    activation_entry.activated = True
    db.session.commit()

    return jsonify({'message': 'User activated successfully'}), 200


def send_activation_email(email):
    message = Message('Account Activation', sender=app.config['MAIL_USERNAME'], recipients=[email])
    message.body = 'Ваш аккаунт активирован! Спасибо за регистрацию!'
    mail.send(message)


app.register_blueprint(registration)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print('Database created')

    app.run(debug=True)
