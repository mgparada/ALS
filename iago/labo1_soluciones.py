#ejemplos antes de labo1
def doble( x ):
	return x * 2

print ( doble( 5 ) )

def inicia():
	return 5, 6

a, b = inicia()
print( a )
print( b )

def foo():
	pass

#Ejercicio 2 labo1
x = raw_input( "Dime tu nombre: " )
print( "Hola, {0:s}".format( x ) )

#Ejercicio 3 labo1

def pedir():
	return raw_input( "Dime tu nombre: " )

def mostrar(x):
	print( "Hola, {0:s}".format( x ) )

x = pedir()
mostrar( x )

#Ejercicio 4 labo1 solucionado con str
#comprobado con int() que se recibieron numeros sino excepcion
def fmtCoordenadas( x, y ):
	try:
		int( x )
		int( y )
		print( "(" + str( x ) + ", " + str( y ) + ")" )
	except Exception:
		print( "Esperando valores coordenadas numericos" )

x = raw_input( "Dame un numero: " )
y = raw_input( "Dame un numero: " )
fmtCoordenadas( x, y )

#Ejercicio 4 con solucionado con format
#comprobado con int() que se recibieron numeros sino excepcion
def fmtCoordenadas( x, y ):
	try:
		int( x )
		int( y )
		print( "({0}, {1})".format( x, y ) )
	except Exception:
		print( "Esperando valores coordenadas numericos" )

x = raw_input( "Dame un numero: " )
y = raw_input( "Dame un numero: " )
fmtCoordenadas( x, y )

#Ejercicio 5
'''se piden dos numeros x e y y un operador z, se repite hasta obtener
valores numericos como operandos y un operador, correcto o incorrecto'''
def pedirNumero():
	try:
		x = float( raw_input( "Introduce el primer operando: " ) )
		y = float( raw_input( "Introduce el segundo operando: " ) )
		z = raw_input( "Introduce el operador: + - * / ^   " )
		return [x,y,z]
	except Exception:
		print( "Operandos no numericos introducidos" )
		return pedirNumero()
		
	
'''se hace la operacion si se ha recibido un operador correcto,
en el caso de la division se contempla el error de division por cero'''
def calculadora(x,y,z):
	if z == '+':
		print ( str( eval( "{0} + {1}".format( x, y) ) ) ) 
	elif z == '-':
		print ( str( eval( "{0} - {1}".format( x, y) ) ) ) 
	elif z == '*':
		print ( str( eval( "{0} * {1}".format( x, y) ) ) ) 
	elif z == '/':
		try:
			print (str(eval("{0} / {1}".format(x,y) ) ) ) 
		except Exception:
			print( "La division no puede ser por cero" )
	elif z == '^':
		print ( str( eval( "{0} ** {1}".format( x, y) ) ) ) 
	else:
		print( "Valor de operador no soportado o erroneo" )


x = pedirNumero()
calculadora(x[0],x[1],x[2])

