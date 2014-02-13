


def mainFunction(l, signo) :
	toret = 0
	if (len(l) > 1) :
		item = l[0]
		if (item == '+' or item == '-' or item == '*' or item == '/') :
			signo = item
			toret = mainFunction(l[1:], item)
			return toret
		else:
			toret = mainFunction(l[1:], signo)
			print(str.format("item {0}", item))
			print(str.format("toret {0}", toret))
			l2 = [toret, item]
			return opera(l2, signo)
	else:
		l2 = [0, l[0]]
		return opera(l2, signo)

# def opera(sign, l) :
# 	tot = {
# 		'+' : suma(l),
# 		'-' : resta(l),
# 		'*' : multiplica(l),
# 		}
# 	return tot[sign]

def opera(l, signo) :
	if (signo == '+') :
		toret = suma(l)
	elif (signo == '-') :
		toret = resta(l)
	elif (signo == '*') :
		toret = multiplica(l)
	return toret

def suma(l) :
	count = 0
	for item in l :
		count += int(item)
	return count

def resta(l) :
	count = 0
	for item in l :
		count += int(item)
	return count

def multiplica(l) :
	count = 1
	for item in l :
		count *= int(item)
	return count





if (__name__ == '__main__') :
	expr = raw_input("Introduce una operacion peixe: ")
	l = expr.split()

	result = list()
	mainFunction(l[1:], l[0])