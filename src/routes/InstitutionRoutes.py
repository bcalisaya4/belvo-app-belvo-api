from flask import Blueprint, request, jsonify

import traceback

## Logger
#from src.utils.Logger import Logger
# Models
from src.models.UserModel import User
## Security
#from src.utils.Security import Security
# Services
from src.services.InstitutionServices import InstitutionServices

institution_bp = Blueprint('institution_bp', __name__)

@institution_bp.route('/institutions')
def list_institutions():
    try:

        # Registrar al usuario mediante AuthService
        institutionServices = InstitutionServices()
        print("Creando institutions router")
        institutions_list = institutionServices.list_institutions()

        return jsonify({'success': True, 'users': institutions_list}), 200

    except Exception as ex:
        # Manejo de errores
        return jsonify({'success': False, 'message': f"Error: {str(ex)}"}), 500
