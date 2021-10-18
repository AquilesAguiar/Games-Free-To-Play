from flask import Blueprint
from src.controllers.index import telaPrincipal

index = Blueprint('/',__name__)


index.route('/')(telaPrincipal)
