from flask import Blueprint, request, jsonify

import traceback

## Logger
#from src.utils.Logger import Logger
# Models
from src.models.UserModel import User
## Security
#from src.utils.Security import Security
# Services
from src.services.AuthService import AuthService

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        email = request.json['email']
        password = request.json['password']
        _user = User(email, password)
        authService = AuthService()
        authenticated_user = authService.login_user(_user)
        if (authenticated_user != None):
            #encoded_token = Security.generate_token(authenticated_user)
            encoded_token = authenticated_user["idToken"]
            return jsonify({'success': True, 'token': f"Bearer {encoded_token}"})
        else:
            response = jsonify({'message': 'Unauthorized'})
            return response, 401
    except Exception as ex:
        print(f"Ocurrió un error: {ex}")
        return jsonify({'message': "ERROR", 'success': False}), 401
        
@auth_bp.route('/logout')
def logout():
    try:
        print("logout services")
        authService = AuthService()
        authenticated_user = authService.logout_user()
        return jsonify({'message': "Session cerrada", 'success': True})
    except Exception as ex:
        print(f"Ocurrió un error: {ex}")
        return jsonify({'message': "ERROR", 'success': False})