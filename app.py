from flask import Flask
from src.routes.index import index
from src.routes.jogos import jogos
from src.routes.detalheJogo import detalheJogo

app = Flask(__name__,template_folder='src\\templates',static_folder='src\\static')

app.register_blueprint(index)
app.register_blueprint(jogos,url_prefix='/jogos')
app.register_blueprint(detalheJogo,url_prefix='/detalheJogo')

if __name__ == '__main__':
    app.run(debug=True)