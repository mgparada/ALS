
def ejercicio2():
	nombre = raw_input("Dime tu nombre: ")
	print("Hola, " + nombre)

#ejercicio2()

#############################

def ejercicio21():
	nombre = raw_input("Dime tu nombre: ")
	print("Hola, %s" % str.format(nombre))

#ejercicio21()

#############################
def ej3PedirNombre():
	return raw_input("Dime tu nombre: ")
	
def ej3VisualizarNombre(nombre):
	print(str.format("Hola, {0}", nombre))
	
#nombre = ej3PedirNombre()
#ej3VisualizarNombre(nombre)
	
###############################
## EJERCICIO 4

def fmtCoordenadas(param1, param2):
	toret = str.format("({0},{1})", param1, param2)
	return toret

def getNumbers():
	param1 = raw_input("Introduce valor1: ")
	param2 = raw_input("Introduce valor2: ")
	return param1, param2

#param1, param2 = getNumbers()
#print(fmtCoordenadas(param1, param2))

#################################
## EJERCICIO 5

def threeParamProgram(n1, n2, signo):
	sign = {"+" : float(n1) + float(n2),
			"-" : float(n1) - float(n2),
			"*" : float(n1) * float(n2),
			"/" : float(n1) / float(n2),
			"**" : float(n1) ** float(n2)
			}
	return sign[signo]

def getThreeParams():
	param1 = raw_input("Introduce valor1: ")
	param2 = raw_input("Introduce valor2: ")
	param3 = raw_input("Introduce signo: ")
	
	try:
		if (float(param1) and float(param2) and str(param3)):
			return param1, param2, param3
	except:
		print("Parametros mal introducidos")


n1, n2, signo = getThreeParams()
print threeParamProgram(n1, n2, signo)

	




	
