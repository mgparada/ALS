
# Si hay un signo AL FINAL se hace un reverse de la lista y luego se llama a la funcion principal
def operaPrefijoPostfijo(l) :
	if (
	        (esSigno(l[0]) == True and esSigno(l[len(l)-1]) == True) or 
	        (esSigno(l[0]) == False and esSigno(l[len(l)-1]) == False) 
		) :			# Valido que no haya signos a principio o al final o que haya en ambos
	      print ("ERROR. Debe haber un signo al principio o al final.")
	elif (esSigno(l[0]) == False ) :
		      l.reverse()	      
	return mainFunction(l[1:], l[0])

def mainFunction(l, signo) :
	item = l[0]
	if (signo == '+' or signo == '-') :
		toret = 0
	else :
		toret = 1
		
	if (len(l) > 1) :
		if (esSigno(item)) :
			toret = mainFunction(l[1:], item)
			return int(toret)
		else:
			toret = int(mainFunction(l[1:], signo)) # mainFunction([3],+)
			l2 = [item, toret]
			return int(opera(l2, signo))
	else:
		l2 = [item, toret] # l2 = [0,3]
		return int(opera(l2, signo))
	
# Si es signo devuelve TRUE, sino FALSE
def esSigno(item) :
	if (item == '+' or item == '-' or item == '*' or item == '/') :
		return True
	else :
		return False

# Segun el signo decide que operacion se realiza
def opera(l, signo) :
	if (signo == '+') :
		toret = suma(l)
	elif (signo == '-') :
		toret = resta(l)
	elif (signo == '*') :
		toret = multiplica(l)
	elif (signo == '/') :
		toret = divide(l)
	return toret

def suma(l) :
	count = 0
	for item in l :
		count += int(item)
	return count

def resta(l) :
	toret = int(l[0]) - int(l[1])
	return toret

def multiplica(l) :
	count = 1
	for item in l :
		count *= int(item)
	return count

def divide(l) :
	print l
	toret = int(l[0]) / int(l[1])
	print toret
	return toret

# Inicio del programa
if (__name__ == '__main__') :
	expr = raw_input("Introduce una operacion peixe: ")
	l = expr.split()

	result = list()
	
	print(str.format("El resultado es: {0}", operaPrefijoPostfijo(l) ))
