def calcular(l,resultado):
	if(len(l)> 3 or len(l) == 3):
		signo = l[0]
		numero = int(l[1])
		del l[0]
		del l[0]
		if (signo =='+'):
			print(resultado)
			resultado=suma(numero,calcular(l,resultado))
		elif(signo == '-'):
			resultado=resta(numero,calcular(l,resultado))
		elif(signo == '*'):
			resultado=mult(numero,calcular(l,resultado))
		elif(signo == '/'):
			resultado=div(numero,calcular(l,resultado))
	else:
		resultado = l[0]
	return resultado

def suma ( numero, resultado):
	resultado = int(numero) + int(resultado)
	return resultado
def resta ( numero, resultado):
	resultado = int(numero) - int(resultado)
	return resultado
def mult ( numero, resultado):
	resultado = int(numero) * int(resultado)
	return resultado
def div ( numero, resultado):
	resultado = int(numero) / int(resultado)
	return resultado


expr=raw_input("Introduce polinomio")
l=expr.split()
print(l)
res=calcular(l,0)
print(res)
