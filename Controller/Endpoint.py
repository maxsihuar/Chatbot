from flask import Blueprint, jsonify,request
from Service import RAG

ChatBot = Blueprint("ChatBot",__name__)

@ChatBot.route("/api/v1/consulta", methods=["POST"])
def PostData():
    """

    """
    data = request.get_json()
    respuesta = RAG.RagMain(data["consulta"])
    return jsonify({"respuesta": respuesta})

