from flask import Blueprint

from src.controllers.jogos import mostrarJogos

jogos = Blueprint('jogos',__name__)


jogos.route('/',methods=['GET'])(mostrarJogos)
