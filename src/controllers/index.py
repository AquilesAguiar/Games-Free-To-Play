from flask import render_template
import requests

def recomendacoes():
    url = 'https://www.freetogame.com/api/games/?sort-by=popularity'
    req = requests.get(url).json()
    req1 = req[0:5]
    req2 = req[5:10]
    return req1,req2

def telaPrincipal():
    jogos1,jogos2 = recomendacoes()
    return render_template("index.html", jogos1=jogos1,jogos2 = jogos2)

        