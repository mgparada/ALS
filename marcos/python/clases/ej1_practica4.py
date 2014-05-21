class Contacto :
	def __init__(self, nombre, email) :
		self.nombre = nombre
		self.email = email

	def getNombre(self) :
		return self.nombre
	
	def getEmail(self) :
		return self.email

	def toString(self) :
		toret = str.format("Nombre: {0}\nEmail: {1}\n", self.nombre, self.email)

		return toret

class Amigo(Contacto) :
	def __init__(self, nombre, email) :
		Contacto.__init__(self, nombre, email)

class Empresa(Contacto) :
	def __init__(self, nombre, email, empresa) :
		Contacto.__init__(self, nombre, email)
		self.empresa = empresa

	def getEmpresa(self) :
		return self.empresa

	def toString(self) :
		toret = Contacto.toString(self)
		toret += str.format("Empresa: {0}\n", self.empresa)
		return toret

class Agenda :
	def __init__(self) :
		self.diccionario = {}
	
	def anhadir(self, c) :
		self.diccionario[c.getNombre()] = c
	
	def borrar(self, n) :
		if (self.diccionario[n] != None) :
			self.diccionario.pop(n)
	
	def buscar(self, n) :
		if (self.diccionario.get(n) != None) :
			#print (str.format("Se ha encontrado al usuario {0}. Su email es {1}", n, diccionario[n]))
			print (self.diccionario[n].toString())
		else :
			print ("No se ha encontrado el contacto")
	
	def toString(self) :
		toret = ""
		print ("Lista de contactos: ")
		for key, value in self.diccionario.items() :
			toret.join(self.diccionario[key].toString())
			print(self.diccionario[key].toString())
		return toret


class Menu :	# clase estatica
	@staticmethod
	def principal() :
		print("1 -> Introducir contacto.")
		print("2 -> Borrar contacto.")
		print("3 -> Buscar contacto.")
		print("4 -> Listar.")
		print("0 -> Salir.")
		opcion = raw_input("Introduce la opcion que corresponda: ")

		return opcion

	@staticmethod
	def nombre() :
		nombre = raw_input("Introduce nombre: ")
		return nombre
	
	@staticmethod
	def email() :
		email = raw_input("Introduce email: ")
		return email

	@staticmethod
	def tipo() :
		tipo = 0
		while (tipo != 1 and tipo != 2) :
			print ("1 -> Es un amigo")
			print ("2 -> Es una empresa")
			tipo = int(raw_input("Elija la opcion que corresponda: "))
		return tipo

	@staticmethod
	def empresa() :
		empresa = raw_input("Introduce tu empresa: ")
		return empresa

	@staticmethod
	def borrar() :
		toDelete = raw_input("Introduce el nombre del usuario que deseas borrar: ")
		return toDelete

	@staticmethod
	def buscar() :
		toSearch = raw_input("Introduce el nombre del usuario que buscas: ")
		return toSearch


def nuevoContacto(agenda) :
	nombre = Menu.nombre()
	email = Menu.email()
	tipo = int(Menu.tipo())

	if (tipo == 1) :
		contacto = Amigo(nombre, email)
	elif (tipo == 2) :
		empresa = Menu.empresa()
		contacto = Empresa(nombre, email, empresa)

	agenda.anhadir(contacto)

def elegirOpcion(opcion, agenda) :
	if (opcion == 1) :
		contacto = nuevoContacto(agenda)
	elif (opcion == 2) :
		toDelete = Menu.borrar()
		agenda.borrar(toDelete)
	elif (opcion == 3) :
		toSearch = Menu.buscar()
		agenda.buscar(toSearch)
	elif (opcion == 4) :
		print(agenda.toString())
		

agenda = Agenda()
opcion = int(20)
while (opcion != 0) :
	opcion = int(Menu.principal())
	if (opcion == 0 or opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4) :
		elegirOpcion(opcion, agenda)





	
