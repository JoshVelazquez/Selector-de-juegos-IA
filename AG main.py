import Compra
import AG
import json

def cargarDatos():
    ruta = "data/juegos.json"
    with open(ruta) as contenido:
        juegos = json.load(contenido)
        return juegos

def main():
    juegos = cargarDatos()
    compra = Compra.Compra(juegos, 2000)
    ag = AG.AG(36, 12, 1, 1800, 0.01, compra)
    ag.run()
    for i in range(len(ag._mejor_historico._cromosoma)):
        if ag._mejor_historico._cromosoma[i] == 1:
            print(juegos[i])

if __name__ == '__main__':
    main()
