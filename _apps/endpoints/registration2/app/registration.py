from flask import request
from flask import jsonify
from flask_bcrypt import Bcrypt

from _apps.endpoints.registration.app import app, db
from _apps.endpoints.registration.models import User, UserActivation, PasswordReset


bcrypt = Bcrypt(app)


@app.route('/auth/users/registration2', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if the email is already registered
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already registered'}), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Check your email for activation instructions'}), 201


@app.route('/auth/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)

    if user is None:
        return jsonify({'message': 'User not found'}), 404

    user_info = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        #'role': user.role,
    }

    return jsonify(user_info), 200


@app.route('/auth/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    user = User.query.get(user_id)

    if user is None:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200

