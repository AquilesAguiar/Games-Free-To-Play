from flask import render_template
import requests

def recomendacoes():
    url = 'https://www.freetogame.com/api/games/?sort-by=popularity'
    req = requests.get(url).json()
    req = req[0:5]
    return req

def telaPrincipal():
    jogos = recomendacoes()
    return render_template("index.html", jogos=jogos)

        