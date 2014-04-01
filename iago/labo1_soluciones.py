#examples before labo1
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

#Exercise 2 labo1
x = raw_input( "What's your name? " )
print( "Hello, {0:s}".format( x ) )

#Exercise 3 labo1

def pedir():
	return raw_input( "What's your name? " )

def mostrar(x):
	print( "Hello, {0:s}".format( x ) )

x = pedir()
mostrar( x )

#Exercise 4 labo1 resolved with function str
#int() test x and y are numbers if not raise exception
def fmtCoordenadas( x, y ):
	try:
		int( x )
		int( y )
		print( "(" + str( x ) + ", " + str( y ) + ")" )
	except Exception:
		print( "Wait for numeric values")

x = raw_input( "Input number: " )
y = raw_input( "Input number: " )
fmtCoordenadas( x, y )

#Exercise 4 resolved with function format
#int() test x and y are numbers if not raise exception
def fmtCoordenadas( x, y ):
	try:
		int( x )
		int( y )
		print( "({0}, {1})".format( x, y ) )
	except Exception:
		print( "Wait for numeric values" )

x = raw_input( "Input number: " )
y = raw_input( "Input number: " )
fmtCoordenadas( x, y )

#Exercise 5
'''Input two operands x and y, input one operator z, repeat to obtain
numeric values to operands and an operador, correct or incorrect'''
def pedirNumero():
	try:
		x = float( raw_input( "Input first operand: " ) )
		y = float( raw_input( "Input second operand: " ) )
		z = raw_input( "Input operator: + - * / ^   " )
		return [x,y,z]
	except Exception:
		print( "Operands not numerics typed" )
		return pedirNumero()
		
	
'''Resolv arithmetic operation if operator is correct,
if operator is / and second operator is zero not operation
is performed'''
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
			print( "Division by zero not permited" )
	elif z == '^':
		print ( str( eval( "{0} ** {1}".format( x, y) ) ) ) 
	else:
		print( "Operator incorrect or not supported" )


x = pedirNumero()
calculadora(x[0],x[1],x[2])

