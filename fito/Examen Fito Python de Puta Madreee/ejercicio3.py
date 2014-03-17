#EJERCICIO 3

def inversa(lista):
	return lista[::-1];

def inversa2(lista):
	lret=[];
	for i in lista:
		lret.insert(0,i);
	return lret;

print(inversa([1,2,3,4]));
print(inversa2([1,2,3,4]));
