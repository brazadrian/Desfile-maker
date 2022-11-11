from flask import Flask, request, render_template
from flask.wrappers import Response
import git

app = Flask(__name__)

@app.route('/')
def galeria():
    return render_template("principal.html")

@app.route('/galeria')
def galeria():
    return render_template("galeria.html")

@app.route('/pecas')
def pecas():
    return render_template("pecas.html")

@app.route('/cardin')
def cardin():
    return render_template("cardin.html")

@app.route('/sobrenos')
def sobre():
    return render_template("sobrenos.html")

@app.route('/voteaqui')
def vote():
    return render_template("voteaqui.html")

@app.route('/arduino')
def principal():
    return render_template("arduino.html")

@app.route('/look1')
def principal():
    return render_template("look1.html")

@app.route('/look2')
def principal():
    return render_template("look2.html")

@app.route('/look3')
def principal():
    return render_template("look3.html")

@app.route('/look4')
def principal():
    return render_template("look4.html")

@app.route('/look5')
def principal():
    return render_template("look5.html")

@app.route('/look6')
def principal():
    return render_template("look6.html")

@app.route('/look7')
def principal():
    return render_template("look7.html")

@app.route('/look8')
def principal():
    return render_template("look8.html")

@app.route('/look9')
def principal():
    return render_template("look9.html")

@app.route('/look10')
def principal():
    return render_template("look10.html")

@app.route('/look11')
def principal():
    return render_template("look11.html")