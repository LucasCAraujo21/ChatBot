from flask import Blueprint
from flask import render_template, request, jsonify, session
from app import responder

from CRUD.service import *
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))    

view = Blueprint("view", __name__)

@view.route("/")
def homepage():
    return render_template("chat.html")


@view.route("/chat", methods=["POST"])
def chat():
    data = request.json
    pergunta = data.get("pergunta")

    resposta = responder(pergunta)

    return jsonify({"resposta": resposta})