import pickle

#Archivos en python

#abrir para escribir texto
f = open ( "archivo.txt", "wt" )

f.write ( "hola\n" )
f.write ( "mundo\n" )
f.close()

#abrir para leer texto
f = open ( "archivo.txt", "rt" )
lines = f.readlines()
f.close()

for line in lines:
	print ( line ),
	
#forma mas segura de leer, pues readlines lee todo 
f = open ( "archivo.txt", "rt" )
try:
	while True:
		line = f.read()
		print( line ),
except:
	pass

f.close()

#abrir para lectura compatible fin de linea linux/windows(\n \n\r)

f = open( "archivo.txt", "rU")
try:
	while True:
		line = f.read()
		print( line ),
except:
	pass

f.close()

#Ejercicio, crear archivo de texto con 10 numeros, uno por linea y hacer lo sig.
'''Se debe leer el archivo de texto, multiplicar cada numero por dos y se
vuelva a escribir el archivo de texto'''
def creaFile():
	f = open( "ej.txt", "wt")
	i = 1
	while i < 11:
		f.write(str(i)+"\n")
		i = i+1
	f.close()

def doblarNum():
	f = open( "ej.txt", "rU")
	l = []
	for line in f:
		num = int(line[0:-1])*2
		l.append(num)
	f.close()
	f = open( "nums.txt", "wt")
	for num in l:
		f.write(str(num)+"\n")
	f.close()	

creaFile()
doblarNum()

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return str.format("({0},{1})",self.x,self.y)




def exercisePersistenceWrite():
	p1 = Point(1,1)
	p2 = Point(2,2)

	f = open ("pic.bin", "wb")
	pickle.dump(p1,f)
	pickle.dump(p2,f)
	f.close()

def exercisePersistenceRead():
	f = open ("pic.bin", "rb")
	p1 = pickle.load(f)
	p2 = pickle.load(f)
	f.close()
	print(p1)
	print(p2)

exercisePersistenceWrite()
exercisePersistenceRead()
