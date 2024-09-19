from flask import Blueprint, request, jsonify

import traceback

## Logger
#from src.utils.Logger import Logger
# Models
from src.models.UserModel import User
## Security
#from src.utils.Security import Security
# Services
from src.services.UserService import UserService

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def register():
    try:
        # Obtener los datos de la solicitud JSON
        email = request.json['email']
        password = request.json['password']

        # Crear una instancia de usuario
        _user = User(email, password)

        # Registrar al usuario mediante AuthService
        userService = UserService()
        new_user = userService.create_user(_user)
        print("Creando usuario router")

        if new_user:
            return jsonify({'success': True, 'message': 'User created successfully'}), 201
        else:
            return jsonify({'success': False, 'message': 'Failed to create user'}), 400

    except Exception as ex:
        # Manejo de errores
        return jsonify({'success': False, 'message': f"Error: {str(ex)}"}), 500



@user_bp.route('/profile')
def get_profile():
    print("profile")
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'success': False, 'message': 'Token not provided'}), 401 
            
        # Eliminar el prefijo 'Bearer' si está presente       
        token = auth_header.split(" ")[1] if "Bearer" in auth_header else auth_header


        userService = UserService()
        user_profile = userService.profile_user(token)
        
        if user_profile:
            return jsonify({'success': True, 'user': user_profile}), 200
        else:
            return jsonify({'success': False, 'message': 'Failed to retrieve profile'}), 400

    except Exception as ex:
        # Manejo de errores
        return jsonify({'success': False, 'message': f"Error: {str(ex)}"}), 500
