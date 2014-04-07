# : en arrays 2:5 por ejemplo, te da una secuencia de numeros

from math import sqrt

## EJERCICIO 1
def media(arr):
	result = 0
	i = 0
	for x in arr:
		result += x
		i += 1
	return result/i
 
def mayor(arr):
	mayor = arr[0]
	for x in arr:
		if (x > mayor):
			mayor = x
	return mayor

def menor(arr):
	menor = arr[0]
	for x in arr:
		if (x > mayor):
			menor = x
	return menor	

def varianza(arr):
	numels = len(arr) - 1
	med = media(arr)
	varianza = 0
	res = 0
	for i in arr:
		res += (i-med)**2
	res /= numels
	return res

def desvTipica(arr):
	return sqrt(varianza(arr))
	

def ejercicio1():
	lista = []
	leer = "jd"
	while ( leer != "0" ):	
		leer = raw_input("Introduce valor: ")
		if ( leer.isdigit() ):
			lista.append(int(leer))
	lista.pop()
	print media(lista)
	print mayor(lista)
	print menor(lista)

	print varianza(lista)
	print desvTipica(lista)

ejercicio1()
		
