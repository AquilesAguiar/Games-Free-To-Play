from flask import Blueprint
from src.controllers.detalheJogo import jogoInfo

detalheJogo = Blueprint("detalheJogo",__name__)

detalheJogo.route('/')(jogoInfo)