#Ejercicio 1 
from math import sqrt

def mayor(x):
	if len(x) > 0:
		return max(x)
	else:
		return 0
		
def menor(x):
	if len(x) > 0:
		return min(x)
	else:
		return 0

def media(x):
	resul = 0.0
	if len(x) > 0:
		for i in range(0,len(x)):
			resul = resul + x[i]
		return resul/len(x)
	else:
		return resul
	
def varianza(x):
	resul = 0.0
	if len(x) > 0:
		for i in range(0,len(x)):
			resul += x[i] ** 2 
		return resul/len(x) - media(x) ** 2
	else:
		return resul
	
def desviacion(x):
	return sqrt(varianza(x))
	
con = []
num = int(raw_input("Introduce un numero: "))
con.append(num)
while num > 0:
	num = int(raw_input("Introduce un numero: "))
	con.append(num)

con.pop(-1)

print("la media es: {0:.2f}".format(media(con)))
print("El maximo es: {0:.2f}".format(mayor(con)))
print("El minimo es: {0:.2f}".format(menor(con)))
print("La desviacion tipica es: {0:.2f}".format(desviacion(con)))

#Solucion labo2 ejercicio 2 notacion prefija
'''se pone primer elemento operador, se comprueba si el siguiente es digito sino
llamada recursiva con el indice donde comienza el nuevo operador encontrado, lo mismo
para el segundo operando, teniendo en cuenta que comienza una posicion a la 
derecha del primer operando'''
def evaluar(cad,indice):
	if len(cad) >= 5:
		op = ['+','-','*','/']
		resul = ''
		op1 = ''
		op2 = ''
		indiceInicial = indice
		lista = cad.split()
		try:
			if lista[indice] in op:
				operator = lista[indice]
				indice+=1;
				if lista[indice].isdigit():
					op1 = lista[indice]
					indice+=1
				else:
					op1, indice = evaluar(cad,indice)		
				if lista[indice].isdigit():
					op2 = lista[indice]
				else:
					op2,indice = evaluar(cad,indice)
				resul += str(float(eval(op1+operator+op2)))
				if indiceInicial == 0:
					print("El resultado de evaluar "+cad+" es {0:.2f}".format(float(resul)))
				else:
					return resul, indiceInicial+3
			else:
				raise Exception("Operador erroneo encontrado: "+lista[indice])
		except TypeError:
			pass
		except Exception as e:
			print(e)
	else:
		print("Expresion demasiado corta para ser evaluada")
		
		
	
		
#prueba funcion evaluar correcta
evaluar('/ - 1 3 * 4 6',0)

#prueba funcion evaluar operador no admitido
evaluar('/ ^ 1 3 * 4 6',0)

#Solucion labo2 ejercicio 2 notacion postfija
'''se pone ultimo elemento operador, se comprueba si el anterior es digito sino
llamada recursiva con el indice donde comienza el nuevo operador encontrado, lo mismo
para el segundo operando, teniendo en cuenta que comienza una posicion a la 
izquierda del primer operando'''
def evaluarPost(cad,indice):
	if len(cad) >= 5:
		op = ['+','-','*','/']
		resul = ''
		op1 = ''
		op2 = ''
		indiceInicial = indice
		lista = cad.split()
		try:
			if lista[indice] in op:
				operator = lista[indice]
				indice-=1
				if lista[indice].isdigit():
					op1 = lista[indice]
					indice-=1
				else:
					op1, indice = evaluarPost(cad,indice)
				if lista[indice].isdigit():
					op2 = lista[indice]
				else:
					op2,indice = evaluarPost(cad,indice)
				resul += str(float(eval(op1+operator+op2)))
				if indiceInicial == -1:
					print("El resultado de evaluar "+cad+" es {0:.2f}".format(float(resul)))
				else:
					return resul, indiceInicial-3
			else:
				raise Exception("Operador erroneo encontrado: "+lista[indice])
		except TypeError:
			pass
		except Exception as e:
			print(e)
	else:
		print("Expresion demasiado corta para ser evaluada")

		
evaluarPost('1 3 4 + +',-1)

#Solucion labo2 ejercicio 2 función que permite evaluar tanto notación prefija como postfija
'''Si los indices son negativos se trata de postfija y si son positivos se trata de prefija'''
def evaluarPreAndPost(cad,indice):
	if len(cad) >= 5:
		op = ['+','-','*','/']
		resul = ''
		op1 = ''
		op2 = ''
		indiceInicial = indice
		lista = cad.split()
		try:
			if lista[indice] in op:
				operator = lista[indice]
				indice = preOrPostIndice(indice)
				if lista[indice].isdigit():
					op1 = lista[indice]
					indice = preOrPostIndice(indice)
				else:
					op1, indice = evaluarPreAndPost(cad,indice)
				if lista[indice].isdigit():
					op2 = lista[indice]
				else:
					op2,indice = evaluarPreAndPost(cad,indice)
				resul += str(float(eval(op1+operator+op2)))
				if indiceInicial == -1 or indiceInicial == 0:
					print("El resultado de evaluar "+cad+" es {0:.2f}".format(float(resul)))
				else:
					if indiceInicial >= 0:
						return resul, preOrPostInicial(indiceInicial)
					else:
						return resul, preOrPostInicial(indiceInicial)
			else:
				raise Exception("Operador erroneo encontrado: "+lista[indice])
		except TypeError:
			pass
		except Exception as e:
			print(e)
	else:
		print("Expresion demasiado corta para ser evaluada")


#Funciones auxiliares de la función evaluarPreAndPost
'''revisa si el indice x pasado como argumento es un indice
de estar evaluando notación prefija o postfija'''
def preOrPostIndice(x):
	if x >=0:
		x+=1
	else:
		x-=1
	return x
	
'''revisa si el indiceInicial x pasado como argumento es el indice de comienzo
de evaluar una expresión y se incrementa(prefija) o decrementa(postfija) en 3 pues 
toda expresión tiene longitud 3, dos operandos y un operador'''	
def preOrPostInicial(x):
	if x >=0:
		x+=3
	else:
		x-=3
	return x
			
#prueba función evaluarPreAndPost con expresión prefija		
evaluarPreAndPost('/ - 1 3 * 4 6',0)

#prueba función evaluarPreAndPost con expresión postfija
evaluarPreAndPost('1 3 4 + +',-1)

#prueba función evaluarPreAndPost con expresión corta
evaluarPreAndPost('1 +',-1)
