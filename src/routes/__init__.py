# routes/__init__.py
#from .IndexRoutes import index_bp
from src.routes.AuthRoutes import auth_bp
from src.routes.UserRoutes import user_bp
from src.routes.InstitutionRoutes import institution_bp
from src.routes.AccountRoutes import account_bp
from src.routes.TransactionRoutes import transaction_bp

def register_blueprints(app):
    # Registrar cada Blueprint en la aplicación principal
    #app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(institution_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(transaction_bp)
    #app.register_blueprint(institute_bp, url_prefix='/institute')