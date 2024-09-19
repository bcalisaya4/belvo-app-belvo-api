import os
from dotenv import load_dotenv
from pathlib import Path

# Ruta hacia el archivo .env
env_path = Path(__file__).resolve().parent / '.env'

# Cargar las variables de entorno
load_dotenv(dotenv_path=env_path)

# Configuración general
class Config:
    
    BELVO_API_URL = os.getenv('BELVO_API_URL')
    BELVO_API_SECRET_ID = os.getenv('BELVO_API_SECRET_ID')
    BELVO_API_SECRET_PASSWORD = os.getenv('BELVO_API_SECRET_PASSWORD')
    
    #API_KEY = os.getenv('API_KEY')
    #DATABASE_URL = os.getenv('DATABASE_URL')
    #DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']

# Otras clases para distintos entornos (opcional)
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Se podría agregar lógica para cargar configuraciones según el entorno
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}