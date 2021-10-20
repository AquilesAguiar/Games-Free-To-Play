from flask import render_template,request
import requests

def jogoInfo():
    id = request.args.get('id')
    url = f"https://www.freetogame.com/api/game?id={id}"
    req = requests.get(url).json()
    return render_template( 'infoJogo.html', jogo=req )
