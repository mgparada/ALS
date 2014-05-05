__author__ = 'mauro'


## Ejercicio 4
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getCoordX(self):
        return self.x

    def getCoordY(self):
        return self.y

    def __str__(self):
        return str.format("({0},{1})", str(self.getCoordX()), str(self.getCoordY()) )


class Linea:
    def __init__(self, inicio, fin):
        self.punto_inicio = inicio
        self.punto_fin = fin

    def getInicio(self):
        return self.punto_inicio

    def getFin(self):
        return self.punto_fin

    def __str__(self):
        return str.format("({0} - {1})", str(self.getInicio()), str(self.getFin()) )

class Poligono:
    def __init__(self, lista):
        self.lista_linea = []
        lista_len =  len(lista)
        cont = 0

        while cont != lista_len:
            self.lista_linea.append( Linea(lista[cont], lista[cont+1]) )
            cont += 2

    def getLineas(self):
        return self.lista_linea

    def __str__(self):
        toRet = ""

        cont = 0
        for l in self.lista_linea:
            cont += 1
            if cont % 2 == 0:
                toRet += " , "

            toRet += str(l)

        return str.format("[ {0} ]", toRet)


print ("--- Ejercicio 4 ---")
p1 = Punto(0, 0)
print("Punto: " + str(p1))

l1 = Linea(p1, Punto(1, 1))
print("Linea: " + str(l1))

poli1 = Poligono([l1.getInicio(), l1.getFin(), Punto(100, 100), Punto(10,20)])
print("Poligono: " + str(poli1))
