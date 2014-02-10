#Ejercicio 1 
from math import sqrt

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
if len(con) > 0:
	print("El maximo es:{0:}".format(max(con)))
	print("El minimo es:{0:}".format(min(con)))
else:
	print("El maximo es: 0")
	print("El minimo es: 0")
print("La desviacion tipica es: {0:.2f}".format(desviacion(con)))




