## Ejercicio 1
def pideNombre():
	nombre = raw_input("Dame tu nombre: ")
	return nombre

def muestraSaludo(nombre):
	print ( str.format("Hola {0}", nombre) )	

## Ejercicio2
def fmtCoordenadas(valor1, valor2):
	print( str.format("Aqui estan los valores: ({0}),({1})", valor1, valor2) )
	print( "Aqui estan los valores: (%s),(%s)" % (valor1, valor2) )

def leerValores():
	valor1 = raw_input("Introduce el valor 1: ")
	valor2 = raw_input("Introduce el valor 2: ")
	return valor1, valor2

## Ejercicio 3
def leerOperacion():
	op = raw_input("Introduce la operacion que quieres \
realizar (+,-,*,/): ")
	while (op != str("+") and op != str("-") and op != str("*") and op != 			str("/") and op != str("^") ):
		print("Has introducido una operacion incorrecta.")
		op = raw_input("Introduce la operacion que quieres \
realizar (+,-,*,/): ")
	
	return op

def realizarOperacion(op, valor1, valor2):
	operaciones = {
		'+': valor1+valor2,
		'-': valor1-valor2,
		'*': valor1*valor2,
		'/': valor1/valor2,
		'^': valor1**valor2
	}
	return str(operaciones[op])


def main():
	## Ejercicio 1
		## muestraSaludo(pideNombre())

	## Ejercicio 2
		## valor1, valor2 = leerValores()
		## fmtCoordenadas(valor1, valor2)
	## Ejercicio 3
	op = leerOperacion()
	valor1, valor2 = leerValores()
	resultado = realizarOperacion(op, float(valor1), float(valor2))
	print ( str.format("El resultado de la operacion {0} {1} {2} es : {3}", 		valor1, op, valor2, resultado ) )

main()
