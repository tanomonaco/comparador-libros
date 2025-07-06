from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola Mundo! Mi sitio web está vivo!"