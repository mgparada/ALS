#EJERCICIO 1

def es_palindromo(cad):
	lista = [];
	for i in cad:
		lista.append(i);
	return lista == lista[::-1];
	
print(es_palindromo("radar"))
