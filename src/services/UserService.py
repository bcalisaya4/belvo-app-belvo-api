#import traceback
#
## Database
#from src.database.db_mysql import get_connection
## Logger
#from src.utils.Logger import Logger
# Models
from src.database.db_firebase import get_connection
from src.models.UserModel import User


class UserService():

    def create_user(self,user):
        print("Creando usuario service 001")
        try:
            print("Creando usuario service 002")
            # Obtener la conexión a Firebase
            connection = get_connection()

            # Crear un nuevo usuario en Firebase Authentication
            auth = connection.auth()
            new_user = auth.create_user_with_email_and_password(user.email, user.password)
            
            return new_user
        except Exception as ex:
            print(f"Error al crear usuario: {ex}")
            return None