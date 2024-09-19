from flask import session
import traceback
#
## Database
from src.database.db_firebase import get_connection
## Logger
#from src.utils.Logger import Logger
## Models
from src.models.UserModel import User


class AuthService():

    #@classmethod
    def login_user(self, user):
        try:
            connection = get_connection()
            auth = connection.auth()
            user_return = auth.sign_in_with_email_and_password(user.email, user.password)
            session['user'] = user.email
            print("session")
            print(session['user'])
            return user_return
        except Exception as ex:
            return 'Faile login'
            #Logger.add_to_log("error", str(ex))
            #Logger.add_to_log("error", traceback.format_exc())
            
    def logout_user(self):
        try:
            #session.pop('user',None)
            print("session")
            #print(session['user'])
            return "Logout Correct"
        except Exception as ex:
            print(f"Ocurrió un error: {ex}")
            return 'Faile logout'
            #Logger.add_to_log("error", str(ex))
            #Logger.add_to_log("error", traceback.format_exc())