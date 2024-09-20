
from flask import Flask
from flask_cors import CORS
from src.routes import register_blueprints

app = Flask(__name__)
CORS(app)
app.secret_key = 'tu_clave_secreta_aqui'

register_blueprints(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)