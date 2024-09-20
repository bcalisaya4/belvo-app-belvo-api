
import requests
from requests.auth import HTTPBasicAuth

from src.database.db_firebase import get_connection
#from src.models.UserModel import User
from config import Config

class TransactionService():

    def list_transactions(self, account_id= None):
        try:
            belvo_api_url = Config.BELVO_API_URL
            belvo_api_secret_id = Config.BELVO_API_SECRET_ID
            belvo_api_secret_password = Config.BELVO_API_SECRET_PASSWORD
            # Obtener la conexión a Firebase
            if account_id:
                response = requests.get(f"{belvo_api_url}/transactions?link__in=dafdee05-56ff-462d-9abb-07d44ce7fe32&account={account_id}", auth=HTTPBasicAuth(belvo_api_secret_id, belvo_api_secret_password))
            else:
                response = requests.get(f"{belvo_api_url}/transactions?link__in=dafdee05-56ff-462d-9abb-07d44ce7fe32", auth=HTTPBasicAuth(belvo_api_secret_id, belvo_api_secret_password))
            
            print("service transaction")
            #response = requests.get(f"{belvo_api_url}/transactions/?link__in=dafdee05-56ff-462d-9abb-07d44ce7fe32", auth=HTTPBasicAuth(belvo_api_secret_id, belvo_api_secret_password))
            if response.status_code == 200:
                print("Solicitud exitosa!")
                # Para ver el contenido de la respuesta en formato JSON
                return response.json()
            else:
                print(f"Error en la solicitud. Código de estado: {response.status_code}")
        except Exception as ex:
            print(f"Error al traer lista: {ex}")
            return None
    
    def info_balance(self, response):
        data = response["results"]
        ingresos = 0
        egresos = 0
        for item in data:
            if item["type"] == "INFLOW":
                ingresos = ingresos + item["amount"]
            elif item["type"] == "OUTFLOW":
                egresos = egresos + item["amount"]
        balance = ingresos - egresos
        return balance