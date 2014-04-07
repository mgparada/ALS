
#EJERCICIO 2

def histograma(lista):
	for i in lista:
		aux="*";
		if(i<=1):
			pass;
		elif(i>11):
			for j in range(11):
				aux+="*";		
		else:
			for j in range(i-1):
				aux+="*";
		print(aux);

histograma([1,2,3,4]);
