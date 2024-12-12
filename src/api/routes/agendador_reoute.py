from flask import Blueprint, jsonify

agendador_bp = Blueprint("agendador", __name__)

@agendador_bp.route("/", methods=["POST"])
def get_users():
    return jsonify({"message": "Esta será a rota para o agendador"}), 200

