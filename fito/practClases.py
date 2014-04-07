class Agenda:
	def __init__(self):
		self.listaContactos = {};
	def anhadir(self, contacto):
		self.listaContactos[contacto.nombre] = contacto;	
	def borrar(self,nombre):
		del(self.listaContactos[nombre]);
	def getElem(self,nombre):
		return self.listaContactos.get(nombre);
	def listado(self):
		mostrar = "";
		for k in self.listaContactos.keys():
			mostrar = str.format("{0}\n {1}" , mostrar , self.listaContactos[k].toString());
		return mostrar; 
				
class Contacto:
	def __init__(self, nombre, email):
		self.nombre = nombre;
		self.email = email;
	def getNombre(self):
		return self.nombre;
	def getEmail(self):
		return self.email;
	def toString(self):
		mostrar =str.format("Nombre: {0}  Email: {1}", self.getNombre(), self.getEmail());
		return mostrar;

class Amigo(Contacto):
	def __init__(self, nombre, email):
		Contacto.__init__(self,nombre,email);
	

class Empresa(Contacto):
	def __init__(self, nombre, email, emailEmpresa):
		Contacto.__init__(self,nombre,email);
		self.emailEmpresa = emailEmpresa;
	def getEmailEmpresa(self):
		return self.emailEmpresa;
	def toString(self):
		mostrar =str.format("{0}  Email de Empresa: {1}", Contacto.toString(self), self.getEmailEmpresa());
		return mostrar;

def introducir():
	nombre=raw_input("Introduce tu nombre o S para cancelar\n");
	if(nombre!="S"):
		email=raw_input("Introduce tu email o S para cancelar\n");
		if(email!="S"):
			opcion=10;	
			while(opcion != 0 ):
				opcion = int(raw_input("Que quieres crear?:\n1.-Amigo\n2.-Empresa\n0.-Cancelar\n"));
				if opcion>2 or opcion <0:
					print("opcion incorrecta\n");
				elif opcion==1:
					contacto = Amigo(nombre , email);
					agenda.anhadir(contacto);
					opcion=0;	
				elif opcion==2:
					emailEmpresa=raw_input("Introduce tu email de la empresa o S para cancelar\n");
					if(emailEmpresa!="S"):
						contacto = Empresa(nombre,email,emailEmpresa);
						agenda.anhadir(contacto);
						opcion=0;
		
					
def borrar():	
	nombre = "i";
	while(nombre!="S"):
		nombre=raw_input("Introduce el nombre de contacto a eliminar o S para cancelar\n");
		if(nombre!="S"):
			if(agenda.getElem(nombre)!=None):
				agenda.borrar(nombre);
			else:
				print("no se encontro elemento\n");
				
def buscar():
	nombre = "i";
	while(nombre!="S"):
		nombre=raw_input("Introduce el nombre de contacto a eliminar o S para cancelar\n");
		if(nombre!="S"):
			contacto = agenda.getElem(nombre);
			if(contacto!=None):
				mostrar = str.format("{0}",contacto.toString());
				print(mostrar); 
			else:
				print("no se encontro elemento\n");
				
def listado():
	mostrar = agenda.listado();
	print (mostrar);

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
			listado();

agenda = Agenda();
menu();





