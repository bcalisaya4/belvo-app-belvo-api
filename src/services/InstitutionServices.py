
import requests
from requests.auth import HTTPBasicAuth

from src.database.db_firebase import get_connection
#from src.models.UserModel import User
from config import Config

class InstitutionServices():
    

    def list_institutions(self):
        try:
            belvo_api_url = Config.BELVO_API_URL
            belvo_api_secret_id = Config.BELVO_API_SECRET_ID
            belvo_api_secret_password = Config.BELVO_API_SECRET_PASSWORD
            # Obtener la conexión a Firebase
            response = requests.get(f"{belvo_api_url}/accounts", auth=HTTPBasicAuth(belvo_api_secret_id, belvo_api_secret_password))
            if response.status_code == 200:
                print("Solicitud exitosa!")
                # Para ver el contenido de la respuesta en formato JSON
                return response.json()
            else:
                print(f"Error en la solicitud. Código de estado: {response.status_code}")
        except Exception as ex:
            print(f"Error al traer lista: {ex}")
            return None