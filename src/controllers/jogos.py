from flask import render_template,request
import requests
from pprint import pprint

def mostrarJogos():
    plataform = request.args.get('platform')

    print(plataform)

    url = "https://www.freetogame.com/api/games?platform=all" if plataform == None  else f"https://www.freetogame.com/api/games?platform={plataform}"
    req = requests.get(url).json()
    return render_template("jogos.html",jogosPlataform=req)