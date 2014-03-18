# 1 Funcion a la que se le pase una lista y devuelva el inverso de esa lista

def inversa(l):
	i = len(l)
	l2 = []
	while (i > 0):
		l2.append(l[i-1])
		i -= 1
	return l2
		
#print( inversa([1,2,3,4,5]) )

# 1 Otra forma

#def inversa2
	l2 = [] # otra forma es l2 = list()
	
	#for i in l:
		#l2[:0] = [i] # l2.insert(0,i)
	#return l2

#print(inversa2([1,2,3,4,5])

# 2 Funcion que devuelve una lista con la sucesion de fibonacci, pasandole un numero que identifica el num de posiciones

def fibo(n):
	l = [1,1]
	i = len(l)

	while ( i < n ):
		aux = l[i-1]+l[i-2]
		l.append(aux)
		i += 1
	return l

#print(fibo(10))

# 3 Funcion a la q se le pasa una lista y devuelve otra lista con los elementos que se repiten mas de una vez en la lista original

def numOccurs(l, elem):
	toret = 0
	for item in l:
		if (item == elem):
			toret += 1
	return toret
	
def repetidos(l):
	lrep = list()

	for item in l:
		if (numOccurs(l, item) == 1):
			lrep.append(item)
	return lrep

#print(numOccurs([1,1,2,3,4,4,5,5,5,5,6,5], 1))
print(repetidos([1,1,2,3,4,4,5,5,5,5,6,5]))
			
			
	














































