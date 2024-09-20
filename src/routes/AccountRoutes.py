from flask import Blueprint, request, jsonify

import traceback

## Logger
#from src.utils.Logger import Logger
# Models
from src.models.UserModel import User
## Security
#from src.utils.Security import Security
# Services
from src.services.AccountService import AccountService

account_bp = Blueprint('account_bp', __name__)

@account_bp.route('/account')
def list_account():
    try:
        institution_name = request.args.get('institution_name', None)  # None es el valor por defecto si no se pasa

        # Registrar al usuario mediante AuthService
        accountService = AccountService()
        if institution_name:
            account_list = accountService.list_account(institution_name)
        else:
            account_list = accountService.list_account()

        return jsonify({'success': True, 'data': account_list["results"]}), 200
    except Exception as ex:
        # Manejo de errores
        return jsonify({'success': False, 'message': f"Error: {str(ex)}"}), 500

        
