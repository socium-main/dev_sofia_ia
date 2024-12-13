from flask import Blueprint, jsonify
from src.agents.tools.check_calendar import check_calendar

agendador_bp = Blueprint("agendador", __name__)

@agendador_bp.route("/buscar_horarios", methods=["GET"])
def get_users():
    response = check_calendar()
    return jsonify({"retorno da funcao": response}), 200
