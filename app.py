from flask import Flask, render_template, request, redirect, url_for
import Compra
import json
import AG
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/juegos")
def getJuegos():
    juegos = cargarDatos()
    return render_template("juegos.html", juegos = juegos)

@app.route("/ejecucion", methods=["POST"])
def ejecucucion():
    if request.method == "POST":
        dinero = request.form["dinero"]
        print(dinero)
        juegosComprados = ejecucionAlgoritmo(dinero)
        numeroJuegos = len(juegosComprados)
        total = 0
        for juego in juegosComprados:
            valor = juego["precio"]
            total = total + valor
        return render_template("resultados.html", juegos = juegosComprados, numeroJuegos = numeroJuegos, total = total)
        

def cargarDatos():
    ruta = "data/juegos.json"
    with open(ruta) as contenido:
        juegos = json.load(contenido)
        return juegos

def ejecucionAlgoritmo(dinero):
    juegos = cargarDatos()
    juegosComprados = []
    compra = Compra.Compra(juegos, float(dinero))
    ag = AG.AG(36, len(juegos), 1, 1800, 0.01, compra)
    ag.run()
    for i in range(len(ag._mejor_historico._cromosoma)):
        if ag._mejor_historico._cromosoma[i] == 1:
            #print(juegos[i])
            juegosComprados.append(juegos[i])
    return juegosComprados



if __name__ == "__main__":
    app.run(debug=True, port=4000)
