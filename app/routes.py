from flask import Blueprint, jsonify, request
from . import db
from .models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({'error':"Data gabisa kosong"}), 404
    
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'error':"Data Duplikat"}), 404
    
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message':"Data Created"}), 201
    
   # Endpoint untuk login dan menghasilkan JWT
@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401

    # Buat JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200

# Endpoint yang membutuhkan autentikasi
@main.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Mendapatkan user yang sedang login dari JWT token
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({"message": f"Hello, {user.username}!"}), 200