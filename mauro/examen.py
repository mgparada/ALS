__author__ = 'mauro'

## Ejercicio 1
def es_palindromo(cadena):
    lista = []
    for i in cadena:
        lista.append(i)

    cont = 0
    ok = True
    for i in cadena[::-1]:
        if lista[cont] == i:
                cont += 1
        else:
            ok = False


    if ok :
        print("La cadena es un palindromo")
    else:
        print("La cadena no es un palindromo")

print ("--- Ejercicio 1 ---")
es_palindromo("casa")
es_palindromo("radar")


## Ejercicio 2
def histograma(lista):
    for i in lista:
        if i >= 11:
            show = "* * * * * * * * * * *"
            print (str.format("{0} -> {1}", show, str(i)))
        else:
            cont = 0
            show = "*"
            while cont != i:
                show += " *"
                cont += 1

            print (str.format("{0} -> {1}", show, str(i)))


print ("--- Ejercicio 2 ---")
histograma([1, 2, 3, 13, 400])

## Ejercicio 3
def inversa(lista):
    lista_inversa = []
    for i in lista[::-1]:
        lista_inversa.append(i)

    print( str.format("La lista inversa de {0} es {1}", lista, lista_inversa) )


print ("--- Ejercicio 3 ---")
inversa([1, 2, 3, 4, 5, 6])

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


## Ejercicio 5

class Estudiante:
    def __init__(self, nombre, email, dni):
        self.nombre = nombre
        self.email = email
        self.dni = dni

    def getNombre(self):
        return self.nombre

    def getDni(self):
        return self.dni

    def getEmail(self):
        return self.email

    def __str__(self):
        return str.format("\n Nombre: {0}\n Dni: {1}\n Email: {2}", self.getNombre(), self.getEmail(), self.getDni())


class EstudianteNormal(Estudiante):
    def __init__(self, nombre, email, dni, provincia):
        Estudiante.__init__(self,nombre, email, dni)
        self.provincia = provincia

    def getProvincia(self):
        return self.provincia


    def __str__(self):
        return str.format("{0}\n Provincia: {1}", Estudiante.__str__(self), self.getProvincia() )


class EstudianteErasmus(Estudiante):
    def __init__(self, nombre, email, dni, pais):
        Estudiante.__init__(self, nombre, email, dni)
        self.pais = pais

    def getPais(self):
        return self.pais

    def __str__(self):
            return str.format("{0}\n Pais: {1}", Estudiante.__str__(self), self.getPais() )

print ("--- Ejercicio 5 ---")

e1 = EstudianteNormal("Mauro", "mgparada@esei.uvigo.es", "55555555A", "Ourense")
print("Estudiante normal: " + str(e1))

e2 = EstudianteErasmus("Aasfas", "asfas@asdaf.com", "45232311242W", "Letonia")
print("Estudiante erasmus: " + str(e2) )