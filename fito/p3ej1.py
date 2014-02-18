def menu():
	opcion=10;
	while(opcion != 0):
		opcion = int(raw_input("Elige una opcion:\n1.-Insertar\n2.-Borrar\n3.-Buscar\n4.-Listar Todo\n0.-Salir\n"));
		if opcion>4 or opcion <0:
			print("opcion incorrecta\n");
		elif opcion==1:
			introducir();	
		elif opcion==2:
			borrar();
		elif opcion==3:
			buscar();
		elif opcion==4 :
			listarTodo();

def listarTodo():
	for k in dic.keys():
		print(str(k) + " : " + str(dic[k])+"\n");
def introducir():
	nombre=raw_input("Introduce tu nombre o S para cancelar\n");
	if(nombre!="S"):
		email=raw_input("Introduce tu email o S para cancelar\n");
		if(email!="S"):	
			dic[nombre] = email;
def borrar():
	nombre="i";
	while(nombre != "S" and nombre == "i"):
		nombre=raw_input("Introduce tu nombre para borrar o S para cancelar\n");
		if(nombre!="S"):
			if(dic.get(nombre)!=None):	
				del(dic[nombre]);
			else:
				print("No se encontro elemento");
				nombre="i";

def buscar():
	nombre="i";
	while(nombre != "S" and nombre == "i"):
		nombre=raw_input("Introduce tu nombre para buscar o S para cancelar\n");
		if(nombre!="S"):
			if(dic.get(nombre)!=None):
				print(nombre + " : " + dic[nombre]);
			else:
				print("No se encontro elemento");
				nombre="i";
dic={}
menu();
