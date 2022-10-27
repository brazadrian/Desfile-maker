from flask import Flask, request, render_template
from flask.wrappers import Response
import git

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("principal.html")

@app.route('/modelo01')
def modelo01():
    return render_template("modelo01.html")

@app.route('/modelo02')
def modelo02():
    return render_template("modelo02.html")