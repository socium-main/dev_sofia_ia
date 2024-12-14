from flask import Blueprint, jsonify
from flask import jsonify, request
from src.agents.builds.sofia_main import sofia_main_graph
from langchain_core.messages import HumanMessage

sofia_bp = Blueprint("sofia", __name__)

@sofia_bp.route("/call", methods=["POST"])
def sofia_call():
    data = request.json
    sofia = sofia_main_graph({"messages": [("user", "what is the weather in sf")]})
    response = sofia.invoke({"messages": [HumanMessage(content=data.get("user_input"))]})
    for r in response['messages']:
        r.pretty_print()
        r.content = r.content.replace("\n", "<br>")
    
    return r.content, 200

