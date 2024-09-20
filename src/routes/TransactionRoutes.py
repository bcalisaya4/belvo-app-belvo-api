from flask import Blueprint, request, jsonify

import traceback

## Logger
#from src.utils.Logger import Logger
# Models
from src.models.UserModel import User
## Security
#from src.utils.Security import Security
# Services
from src.services.TransactionService import TransactionService

transaction_bp = Blueprint('transaction_bp', __name__)

@transaction_bp.route('/transactions')
def list_transactions():
    try:
        account_id = request.args.get('account_id', None)  # None es el valor por defecto si no se pasa

        # Registrar al usuario mediante AuthService
        transactionService = TransactionService()
        transactions_list = None
        if account_id:
            transactions_list = transactionService.list_transactions(account_id)
            balance = transactionService.info_balance(transactions_list)
        else:
            transactions_list = transactionService.list_transactions()
        return jsonify({'success': True, 'data': transactions_list["results"], 'balance': balance}), 200
    except Exception as ex:
        # Manejo de errores
        return jsonify({'success': False, 'message': f"Error: {str(ex)}"}), 500
