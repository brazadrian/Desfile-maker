from flask import Flask, request, render_template
from flask.wrappers import Response
import git

app = Flask(__name__)

@app.route('/galeria')
def galeria():
    return render_template("galeria.html")

@app.route('/pecas')
def pecas():
    return render_template("peças.html")

@app.route('/cardin')
def cardin():
    return render_template("cardin.html")

@app.route('/sobrenos')
def sobre():
    return render_template("sobrenos.html")

@app.route('/voteaqui')
def vote():
    return render_template("voteaqui.html")

@app.route('/')
def principal():
    return render_template("principal.html")