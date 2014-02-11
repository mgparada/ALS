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
			aux = len(op1)+len(operator)+len(op2)
			resul += str(float(eval(op1+operator+op2)))
			if indiceInicial == 0:
				print("El resultado de evaluar "+cad+" es {0:.2f}".format(float(resul)))
			else:
				return resul, indiceInicial+aux
		else:
			raise Exception("Operador erroneo encontrado: "+lista[indice])
	except TypeError:
		pass
	except Exception as e:
		print(e)
		
		
	
		
#prueba funcion evaluar correcta
evaluar('/ - 1 3 * 4 6',0)

#prueba funcion evaluar operador no admitido
evaluar('/ ^ 1 3 * 4 6',0)



