from src.api.routes.home_route import home_bp
from src.api.routes.sofia_route import sofia_bp
from src.api.routes.agendador_route import agendador_bp

def register_blueprints(app):
    app.register_blueprint(home_bp, url_prefix="/home")
    app.register_blueprint(sofia_bp, url_prefix="/sofia")
    app.register_blueprint(agendador_bp, url_prefix="/agendador")