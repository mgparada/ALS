# Dinamicidad en python

class Point:
	def __init__(self, a, b):
		self.x = a
		self.y = b

def Point_getX(self):
	return self.x

def Point_getY(self):
	return self.y

def Point_str(self):
	return str(self.x) + ", " + str(self.y)

Point.getX = Point_getX
Point.getY = Point_getY


## FUNCION LISTAMIEMBROS: devuelve una lista los miembros de un objeto pasado por parametro
## Si es un atributo, imprime su valor: nom_attr '=' 'valor'
## Si es un metodo imprime: 'met()'

def listamiembros(obj):
	toret = []	
	lm = dir(obj)
	for m in lm:
		member = getattr(obj, m)
		if (callable(member)):
			toret.append(m + "()")
		else:
			toret.append(m + " = " + str(member) )
	return toret

p1 = Point(5,6)
listamiembros(p1)


class A:
	def __getattr__(self, x):
		if (x == "test"):
			return 1
		else:
			return 0

p1 = Point(5,6)
## getattr, en caso de existir, intercepta las llamadas a cualquier miembro de la clase
## a = A()
#a.x -> 0
#a.test = 1
#a.z = 10
#a.z
## Si accedo a a.z sin existir, automaticamente se llama a getattr (se intercepta la llamada).





## Posibles pruebas
# listamiembros(p1)
# p1.__dict__["y"] -> 6
# p1.__dict__["x"] -> 5
# Point.__dict__

# diez = eval("5*2")
# diez = eval("p1.getX()*2")
# exec("def f(x): return x * 2")	# compilamos una funcion y accedemos
# f(8)

## Posibles pruebas

#p1 = Point(5,6)
#p1.getX()
#p1.getY()
#def Point_str(self):
#	return ....

#?p1.z = 3
# dir(p1)
# del(p1.z)

# for m in dir(p1):
#	print m

## Saber si es posible llamar a alguien: CALLABLE(var)
# callable(p1.x) -> false
# callable(p1.getX) -> true

# getattr(p1, "x") -> 100
# getattr(p1, "y") -> 6

# Objeto:
# - Leer sus miembros: 		dir(obj)
# - Anhadir un miembro: 	obj.miembro = ... metodo atributo etc
# - Modificar un miembro: 	obj.miembro = ...
# - Eliminar un miembro:	del obj.miembro 	
