from flask import Flask, request, render_template
from flask.wrappers import Response
import git

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("principal.html")

@app.route('/modelo1')
def modeloUm():
    return render_template("modelo_Um.html")

@app.route('/modelo2')
def modeloDois():
    return render_template("modelo_Dois.html")