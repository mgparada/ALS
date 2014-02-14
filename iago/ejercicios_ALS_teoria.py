# 1 Function inversa
''' param l is a list
param return l2 is reverse list of list l'''

def inversa(l):
	i = len(l)
	l2 = []
	while i > 0:
		l2.append(l[i-1])
		i -= 1
	return l2
		
print( inversa([1,2,3,4,5]) )

# 1 Second solution of inversa

def inversa2
	l2 = [] 
	
	for i in l:
		l2[:0] = [i] # l2.insert(0,i)
	return l2

print(inversa2([1,2,3,4,5])

# 2 Function fibonacci
'''param n is a number to indicate how many values of the sequence of fibonacci display'''
def fibo(n):
	l = [1,1]
	i = len(l)

	while i < n :
		aux = l[i-1]+l[i-2]
		l.append(aux)
		i += 1
	return l

print(fibo(10))

# 3 function to display recurrent values in list l

#function to know if a elem appeared more once in list l
def numOccurs(l, elem):
	toret = 0
	for item in l:
		if item == elem:
			toret += 1
	return toret
	
#fucntion to display recurrent values	
def repetidos(l):
	lrep = list()

	for item in l:
		if numOccurs(l, item) > 1 and not item in lrep:
			lrep.append(item)
	return lrep

print(numOccurs([1,1,2,3,4,4,5,5,5,5,6,5], 1))
print(repetidos([1,1,2,3,4,4,5,5,5,5,6,5]))

#solution repetidos in class 11 febrero 2014
def repetidos2(lista):
	aux = []
	l = []
	for x in lista:
		i = 0
		while i < len(aux):
			if x == aux[i][0]:
				aux[i][1]+=1
				break
			i+=1
		if i >= len(aux):
			aux.append([x,1])

	for x in aux:
		if x[1] > 1:
			l.append(x[0])
	return l
	
#test function repetidos class version 
print(repetidos2([1,1,3,3,4]))
