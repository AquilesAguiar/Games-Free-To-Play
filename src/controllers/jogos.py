from flask import render_template,request
import requests

def mostrarJogos():
    plataform = request.args.get('plataform')
    
    url = "https://www.freetogame.com/api/games?platform=all" if plataform == None  else f"https://www.freetogame.com/api/games?platform={plataform}"
    req = requests.get(url).json()
    
    return render_template("jogos.html",jogosPlataform=req)