import math

def insertNumber():
	num = -1
	listNumbers = []
	while num != str("0") :
		num = raw_input("Introduce un numero (0 para terminar): ")
		if num.isdigit():
			listNumbers.append(int(num))

	listNumbers.pop()
	return listNumbers

def getMinus(myList):
	minus = myList[0]
	for item in myList:
		if int(item) < int(minus):
			minus = item
	return minus

def getMayor(myList):
	mayor = myList[0]
	for item in myList:
		if int(item) > int(mayor):
			mayor = item
	return mayor

def getSuma(myList):
	suma = 0
	for item in myList:
		suma += int(item)

	return suma

def getMedia(myList):
	suma = getSuma(myList)
	length = len(myList)
	
	return suma/length

def getVarianza(myList):
	length = len(myList)
	media = getMedia(myList)

	suma = 0		
	for item in myList:
		suma += (int(item) - media)**2

	total =	suma/(length-1)

	return math.sqrt(total)

def main():
	myList = insertNumber()
	minus = getMinus(myList)
	mayor = getMayor(myList)
	suma = getSuma(myList)
	media = getMedia(myList)
	varianza = getVarianza(myList)
	print( str.format("El numero menor es {0} \nEl numero mayor es {1} \nLa suma es {2} \nLa media es {3} \nLa varianza es {4}", minus,mayor, suma, media, varianza) )


main()

