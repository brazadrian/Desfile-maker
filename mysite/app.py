from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template,json
from flask.wrappers import Response
import git
from datetime import datetime
import os
import time

os.environ["TZ"] = "America/Recife"
time.tzset()

header_key = '*'

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Recnplay2022:2507phph@Recnplay2022.mysql.pythonanywhere-services.com/Recnplay2022$default'
db = SQLAlchemy(app)

class votos(db.Model):
    id_voto = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(20))
    hora = db.Column(db.Time)
    nome_modelo = db.Column(db.String(20),nullable=False)

    def to_json(self):
        return {"id": self.id_voto,"data": self.data, "hora": self.hora, "nome_modelo": self.nome_modelo }

class curtidas(db.Model):
    id_curtida = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(20))
    hora = db.Column(db.Time)
    nome_modelo = db.Column(db.String(20),nullable=False)

    def to_json(self):
        return {"id": self.id_voto,"data": self.data, "hora": self.hora, "nome_modelo": self.nome_modelo}


###Rotas

@app.route('/galeria')
def galeria():
    return render_template("galeria.html")

@app.route('/look1')
def look1():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play1"))
        return render_template("look1.html", curtida=curtido.count() )
    except :
        return render_template("look1.html", curtida="try" )

@app.route('/look2')
def look2():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play2"))
        return render_template('look2.html', curtida=curtido.count())
    except :
        return render_template('look2.html', curtida="try")

@app.route('/look3')
def look3():
    try:
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play3"))
        return render_template('look3.html', curtida=curtido.count())
    except :
        return render_template('look3.html', curtida="try")

@app.route('/look4')
def look4():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play4"))
        return render_template('look4.html', curtida=curtido.count())
    except :
        return render_template('look4.html', curtida="try")

@app.route('/look5')
def look5():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play5"))
        return render_template('look5.html', curtida=curtido.count())
    except :
        return render_template('look5.html', curtida="try")

@app.route('/look6')
def look6():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play6"))
        return render_template('look6.html', curtida=curtido.count())
    except :
        return render_template('look6.html', curtida="try")


@app.route('/look7')
def look7():
    try:
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play7"))
        return render_template('look7.html', curtida=curtido.count())
    except :
        return render_template('look7.html', curtida="try")

@app.route('/look8')
def look8():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play8"))
        return render_template('look8.html', curtida=curtido.count())
    except :
        return render_template('look8.html', curtida="try")

@app.route('/look9')
def look9():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play9"))
        return render_template('look9.html', curtida=curtido.count())
    except :
        return render_template('look9.html', curtida="try")

@app.route('/look10')
def look10():
    try :
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play10"))
        return render_template('look10.html', curtida=curtido.count())
    except :
        return render_template('look10.html', curtida="try")

@app.route('/look11')
def look11():
    try:
        curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play11"))
        return render_template('look11.html', curtida=curtido.count())
    except :
        return render_template('look11.html', curtida="try")


@app.route('/cardin')
def cardin():
    return render_template("cardin.html")

@app.route('/sobrenos')
def sobre():
    return render_template("sobrenos.html")

@app.route('/votacao')
def vote():
    return render_template("votacao.html")

@app.route('/')
def principal():
    return render_template("principal.html")


@app.route('/voto')
def inserir():
    data, hora = takeDataHora()
    nome_modelo=str("Rec's n Play")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()

    return render_template("look1.html")

@app.route('/voto2')
def inserir2():
    data, hora = takeDataHora()
    nome_modelo=str("M02")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look2.html")

@app.route('/voto3')
def inserir3():
    data, hora = takeDataHora()
    nome_modelo=str("M03")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look3.html")

@app.route('/voto4')
def inserir4():
    data, hora = takeDataHora()
    nome_modelo=str("M04")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look4.html")

@app.route('/voto5')
def inserir5():
    data, hora = takeDataHora()
    nome_modelo=str("M05")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look5.html")

@app.route('/voto6')
def inserir6():
    data, hora = takeDataHora()
    nome_modelo=str("M06")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look6.html")

@app.route('/voto7')
def inserir7():
    data, hora = takeDataHora()
    nome_modelo=str("M07")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look7.html")

@app.route('/voto8')
def inserir8():
    data, hora = takeDataHora()
    nome_modelo=str("M08")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look8.html")

@app.route('/voto9')
def inserir9():
    data, hora = takeDataHora()
    nome_modelo=str("M09")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look9.html")

@app.route('/voto10')
def inserir10():
    data, hora = takeDataHora()
    nome_modelo=str("M10")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look10.html")

@app.route('/voto11')
def inserir11():
    data, hora = takeDataHora()
    nome_modelo=str("M11")
    novo = votos(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return render_template("look11.html")

@app.route('/curtida', methods = ['GET','POST'])
def curtir1():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play1")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play1"))
            return render_template("look1.html", curtida=curtido.count() )
        except :
            return render_template("look1.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play1"))
            return render_template("look1.html", curtida=curtido.count() )
        except :
            return render_template("look1.html", curtida="try" )


@app.route('/curtida2', methods = ['GET','POST'])
def curtir2():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play2")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play2"))
            return render_template("look2.html", curtida=curtido.count() )
        except :
            return render_template("look2.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play2"))
            return render_template("look2.html", curtida=curtido.count() )
        except :
            return render_template("look2.html", curtida="try" )

@app.route('/curtida3', methods = ['GET','POST'])
def curtir3():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play3")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play3"))
            return render_template("look3.html", curtida=curtido.count() )
        except :
            return render_template("look3.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play3"))
            return render_template("look3.html", curtida=curtido.count() )
        except :
            return render_template("look3.html", curtida="try" )

@app.route('/curtida4', methods = ['GET','POST'])
def curtir4():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play4")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play4"))
            return render_template("look4.html", curtida=curtido.count() )
        except :
            return render_template("look4.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play4"))
            return render_template("look4.html", curtida=curtido.count() )
        except :
            return render_template("look4.html", curtida="try" )

@app.route('/curtida5', methods = ['GET','POST'])
def curtir5():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play5")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play5"))
            return render_template("look5.html", curtida=curtido.count() )
        except :
            return render_template("look5.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play5"))
            return render_template("look5.html", curtida=curtido.count() )
        except :
            return render_template("look5.html", curtida="try" )

@app.route('/curtida6', methods = ['GET','POST'])
def curtir6():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play6")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play6"))
            return render_template("look6.html", curtida=curtido.count() )
        except :
            return render_template("look6.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play6"))
            return render_template("look6.html", curtida=curtido.count() )
        except :
            return render_template("look6.html", curtida="try" )

@app.route('/curtida7', methods = ['GET','POST'])
def curtir7():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play7")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play7"))
            return render_template("look7.html", curtida=curtido.count() )
        except :
            return render_template("look7.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play7"))
            return render_template("look7.html", curtida=curtido.count() )
        except :
            return render_template("look7.html", curtida="try" )

@app.route('/curtida8', methods = ['GET','POST'])
def curtir8():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play8")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play8"))
            return render_template("look8.html", curtida=curtido.count() )
        except :
            return render_template("look8.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play8"))
            return render_template("look8.html", curtida=curtido.count() )
        except :
            return render_template("look8.html", curtida="try" )

@app.route('/curtida9', methods = ['GET','POST'])
def curtir9():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play9")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play9"))
            return render_template("look9.html", curtida=curtido.count() )
        except :
            return render_template("look9.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play9"))
            return render_template("look9.html", curtida=curtido.count() )
        except :
            return render_template("look9.html", curtida="try" )

@app.route('/curtida10', methods = ['GET','POST'])
def curtir10():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play10")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play10"))
            return render_template("look10.html", curtida=curtido.count() )
        except :
            return render_template("look10.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play10"))
            return render_template("look10.html", curtida=curtido.count() )
        except :
            return render_template("look10.html", curtida="try" )

@app.route('/curtida11', methods = ['GET','POST'])
def curtir11():
    if request.method == 'POST' :
        try:
            data, hora = takeDataHora()
            nome_modelo=str("Play11")
            novo = curtidas(data=data,hora=hora, nome_modelo=nome_modelo)
            db.session.add(novo)
            db.session.commit()
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play11"))
            return render_template("look11.html", curtida=curtido.count() )
        except :
            return render_template("look11.html", curtida="try" )
    else : # se o methodo for GET ou outro
        try :
            curtido = curtidas.query.filter(curtidas.nome_modelo.like("Play11"))
            return render_template("look11.html", curtida=curtido.count() )
        except :
            return render_template("look11.html", curtida="try" )

def takeDataHora():
    data = str(datetime.today().strftime("%d/%m/%Y"))
    hora = str(datetime.time(datetime.now()))
    hora = hora[0:8]
    return data, hora

@app.route('/consulta')
def consulta():
    consulta = curtidas.query.filter(curtidas.nome_modelo.like("Play1"))
    return str(consulta.count())

@app.route('/busca', methods=['GET'])
def busca():
    consulta=  curtidas.query.all()
    curtir=[]
    for c in consulta:
        curtir.append({'id': c.id_voto,'data': c.data, 'hora': c.hora, 'nome do modelo': c.nome_modelo })
    return json.dumps(curtir)

###Funções Arduíno

@app.route('/setamodelo', methods=['GET','POST'])
def setamodelo():
    dados = request.get_json()
    valor = dados["valor"]
    global statusModeloUm
    statusModeloUm = valor
    return {"Stat modelo um": statusModeloUm}

@app.route('/statusmodeloum', methods=['GET', 'POST'])
def testaget():
    global statusModeloUm
    valor = statusModeloUm
    statusModeloUm = "Null"
    return {"Modelo Um": str(valor)}

if __name__ == '__main__':
    app.run()