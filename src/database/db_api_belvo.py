
import requests
from requests.auth import HTTPBasicAuth


def get_connection(endpoint):
    # URL de la API
    url = "https://sandbox.belvo.com/api/{endpoint}/"

    # Tus credenciales de autenticación
    username = "5b445697-0d9a-45c0-b037-0bd73e9d48f5"
    password = "bOyR8ir3HfGsg-kfhXXo6GnFhb78r#PMNilbyQPDozMOs8h_UdgzO9yWmhDhwtS@"

    #return HTTPBasicAuth(username, password)
    # # Hacer la solicitud GET con autenticación básica
    # requests.get(url, auth=HTTPBasicAuth(username, password))
    # # Verificar si la solicitud fue exitosa
    # if response.status_code == 200:
    #     print("Solicitud exitosa!")
    #     print(response.json())  # Para ver el contenido de la respuesta en formato JSON
    # else:
    #     print(f"Error en la solicitud. Código de estado: {response.status_code}")
