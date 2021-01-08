class Compra:
    def __init__(self, listaVideojuegos, dineroTotal):
        self.listaVideojuegos = listaVideojuegos
        self.dineroTotal = dineroTotal

    def f(self, cromosoma):
        f = 0
        total = 0
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                f = f + self.listaVideojuegos[i]["precio"]
                total = total + self.listaVideojuegos[i]["precio"]

        if total <= self.dineroTotal:
            return f
        else:
            return 0


class Juegos:
    def __init__(self, nombre, precio, imagen):
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
