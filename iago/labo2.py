#Exercise 1 
from math import sqrt

def mayor(x):
	if len(x) > 0:
		return max(x)
	else:
		return 0
		
def menor(x):
	if len(x) > 0:
		return min(x)
	else:
		return 0

def media(x):
	resul = 0.0
	if len(x) > 0:
		for i in range(0,len(x)):
			resul = resul + x[i]
		return resul/len(x)
	else:
		return resul
	
def varianza(x):
	resul = 0.0
	if len(x) > 0:
		for i in range(0,len(x)):
			resul += x[i] ** 2 
		return resul/len(x) - media(x) ** 2
	else:
		return resul
	
def desviacion(x):
	return sqrt(varianza(x))
	
con = []
num = int(raw_input("Input number: "))
con.append(num)
while num > 0:
	num = int(raw_input("Input number: "))
	con.append(num)

con.pop(-1)

print("Average is: {0:.2f}".format(media(con)))
print("Maximum is: {0:.2f}".format(mayor(con)))
print("Minimum is: {0:.2f}".format(menor(con)))
print("Typical deviation is: {0:.2f}".format(desviacion(con)))



#Solution labo2 exercise 2 arithmetic prefix notation

'''ONLY INTEGER NUMBERS IN EXPRESSIONS, FLOAT NUMBERS NOT SUPPORTED!!!'''

'''First elem is operator, next is digit if not 
recursive function call with index where start new operator found, same
to second operand, second operand always start one position to right of 
first operand'''
def evaluar(cad,index):
	if len(cad) >= 5:
		if cad[0] in '+-*/' and cad[-1] not in '+-*/':
			resul = ''
			op1 = ''
			op2 = ''
			indiceInicial = index
			lista = cad.split()
			try:
				if lista[index] in '+-*/':
					operator = lista[index]
					index+=1
					if lista[index].isdigit():
						op1 = lista[index]
						index+=1
					else:
						op1, index= evaluar(cad,index)		
						if lista[index].isdigit():
							op2 = lista[index]
						else:
							op2,index = evaluar(cad,index)
						#op2 can be 0 or 0.0
						if  (float(op2) == 0) and operator == '/':
							raise Exception("Divison by zero found")
						else:
							resul += str(float(eval(str(float(op1))+operator+str(float(op2)))))
						if indiceInicial == 0:
							return "The resul of eval "+cad+" is {0:.2f}".format(float(resul))
						else:
							return resul, index+1
					if index<=len(lista)-1:
						if lista[index].isdigit():
							op2 = lista[index]
						else:
							op2,index = evaluar(cad,index)
						if  (float(op2) == 0) and operator == '/':
							raise Exception("Divison by zero found")
						else:
							resul += str(float(eval(str(float(op1))+operator+str(float(op2)))))
						if indiceInicial == 0:
							return "The resul of eval "+cad+" is {0:.2f}".format(float(resul))
						else:
							return resul, index+1
				else:
					raise Exception("Operator incorrect found: "+lista[index])
			except TypeError:
				pass
			except Exception as e:
				print(e)
		else:
			print("Expression can't start and finish by operator at same time")
	else:
		print("Expression too short to be evaluated")
		
		
	
		
#test function evaluar correct
resul = evaluar('/ - 1 3 * 4 6',0)
print(resul)

#test function evaluar operator not admitted
evaluar('/ ^ 1 3 * 4 6',0)

#test evaluar large expression
resul = evaluar('- - - - 4 7 - 6 5 - - 3 2 - 1 6 - - - 2 4 - 3 2 - - 1 2 - 3 4',0)
print(resul)

#Solution labo2 exercise 2 arithmetic postfix notation
'''Last elem is operator, previous is digit if not 
recursive function call with index where start new operator found, same
to second operand, second operand always start one position to left of 
first operand'''
def evaluarPost(cad,index):
	if len(cad) >= 5:
		if cad[0] not in '+-*/' and cad[-1] in '+-*/':
			resul = ''
			op1 = ''
			op2 = ''
			indiceInicial = index
			lista = cad.split()
			try:
				if lista[index] in '+-*/':
					operator = lista[index]
					index-=1
					if lista[index].isdigit():
						op1 = lista[index]
						index-=1
					else:
						op1, index= evaluarPost(cad,index)		
						if lista[index].isdigit():
							op2 = lista[index]
						else:
							op2,index = evaluarPost(cad,index)
						if  (float(op2) == 0) and operator == '/':
							raise Exception("Divison by zero found")
						else:
							resul += str(float(eval(str(float(op1))+operator+str(float(op2)))))
						if indiceInicial == -1:
							return "The resul of eval "+cad+" is {0:.2f}".format(float(resul))
						else:
							return resul, index-1
					if index<=0:
						if lista[index].isdigit():
							op2 = lista[index]
						else:
							op2,index = evaluarPost(cad,index)
						if  (float(op2) == 0) and operator == '/':
							raise Exception("Divison by zero found")
						else:
							resul += str(float(eval(str(float(op1))+operator+str(float(op2)))))
						if indiceInicial == -1:
							return "The resul of eval "+cad+" is {0:.2f}".format(float(resul))
						else:
							return resul, index-1
				else:
					raise Exception("Operator incorrect found: "+lista[index])
			except TypeError:
				pass
			except Exception as e:
				print(e)
		else:
			print("Expression can't start and finish by operator at same time")
	else:
		print("Expression too short to be evaluated")
		
resul = evaluarPost('1 3 4 + +',-1)
print(resul)

#Solution labo2 exercise 2 function to eval  both arithmetic prefix and postfix notation
'''Negative index postfix notation and positive index prefix notation'''
def evaluarPreAndPost(cad,index):
	if len(cad) >= 5:
		#In python ^ is the operator: or exclusive!!!
		if (cad[0] in '+-*/') ^ (cad[-1] in '+-*/'):
			resul = ''
			op1 = ''
			op2 = ''
			indiceInicial = index
			lista = cad.split()
			try:
				if lista[index] in '+-*/':
					operator = lista[index]
					index = preOrPostIndice(index)
					if lista[index].isdigit():
						op1 = lista[index]
						index = preOrPostIndice(index)
					else:
						op1, index= evaluarPreAndPost(cad,index)		
						if lista[index].isdigit():
							op2 = lista[index]
						else:
							op2,index = evaluarPreAndPost(cad,index)
						if  (float(op2) == 0) and operator == '/':
							raise Exception("Divison by zero found")
						else:
							resul += str(float(eval(str(float(op1))+operator+str(float(op2)))))
						if indiceInicial == -1 or indiceInicial == 0 :
							return "The resul of eval "+cad+" is {0:.2f}".format(float(resul))
						else:
							index = preOrPostIndice(index)
							return resul, index
					if index<=0 or index <=len(lista)-1:
						if lista[index].isdigit():
							op2 = lista[index]
						else:
							op2,index = evaluar(cad,index)
						if  (float(op2) == 0) and operator == '/':
							raise Exception("Divison by zero found")
						else:
							resul += str(float(eval(str(float(op1))+operator+str(float(op2)))))
						if indiceInicial == -1 or indiceInicial == 0:
							return "The resul of eval "+cad+" is {0:.2f}".format(float(resul))
						else:
							index = preOrPostIndice(index) 
							return resul, index
				else:
					raise Exception("Operator incorrect found: "+lista[index])
			except TypeError:
				pass
			except Exception as e:
				print(e)
		else:
			print("Expression can't start and finish by operator at same time")
	else:
		print("Expression too short to be evaluated")


#Auxiliary function of function evaluarPreAndPost
'''text index x received as param is a index
of eval prefix notation or postfix notation'''
def preOrPostIndice(x):
	if x >=0:
		x+=1
	else:
		x-=1
	return x

#test function evaluarPreAndPost with prefix expression		
resul = evaluarPreAndPost('/ - 1 3 * 4 6',0)
print(resul)

#test function evaluarPreAndPost with postfix expression
resul = evaluarPreAndPost('1 3 4 + +',-1)
print(resul)

#test function evaluarPreAndPost with short expression 
evaluarPreAndPost('1 +',-1)
