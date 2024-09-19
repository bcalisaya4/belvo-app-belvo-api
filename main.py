#from src import init_app
#from config import config
#
#configuration = config['development']
#app = init_app(configuration)
from flask import Flask
from src.routes import register_blueprints

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)