from flask import Blueprint, jsonify

sofia_bp = Blueprint("sofia", __name__)

@sofia_bp.route("/", methods=["POST"])
def get_users():
    return jsonify({"message": "Esta será a rota para a sofia"}), 200

