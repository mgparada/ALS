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

'''Therory Class notes February 17, 2014'''

#Dictionaries
'''Two declarations for a dictionary'''
d1 = dict()
d2 = {}


temperaturas = { "Vigo": 10.5, "Ourense": 7.2 }

#Prin a value associated a Key Vigo
print( temperaturas[ "Vigo" ] )

#Insert/modify an element
temperaturas[ "Oviedo"] = 8.5
print( temperaturas[ "Oviedo" ] )

#Print all elements dictionary
for k,v in temperaturas.items():
    print( k + ": " + str( v ) )
    
#Obtanin value of an element what aren't in dcitionary give value None
tempBarcelona = temperaturas.get( "Barcelona" )


if tempBarcelona != None:
    print( "Barcelona: " + str( tempBarcelona ) )
else:
    print( "No hay datos de temperatura para esa ciudad" )
    
#Exercise repetidos with dictionary

def repetDiccionario(l):
    result = []
    dic = {}
    i = 0
    for i in l:
        if dic.get(i) == None:
            dic[i] = 1
        else:
            dic[i] += 1
        i+=1
    for k,v in dic.items():
        if v > 1:
            result.append(k)
    return result
    
#test function repetDiccionario            
print( "Repetidos: " + str(repetDiccionario([1,1,2,3,4,4])))

'''Function what count words, recive a string s and return
occur frecuency of a word'''
def cuentaPalabra(s):
    dic = {}
    i = 0
    for i in s.strip().split():
        if dic.get(i) == None:
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)

#Test function cuentaPalabra with string in Spanish Language    
cuentaPalabra("El perro de la huerta marrón es marrón")
    
    
