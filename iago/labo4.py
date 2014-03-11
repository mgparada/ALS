#Menu not finished

class Contacto:
	def __init__( self, name, email ):
		self.name = name
		self.email = email

	def getName( self ):
		return self.name

	def getEmail( self ):
		return self.email

	def __str__( self ):
		return str.format(" Nombre: {0}\n Email: {1}\n",
					self.getName(),
					self.getEmail())

class Amigo(Contacto):
	def __init__( self, name, email):
		Contacto.__init__( self,name, email)
	

class Trabajo(Contacto):
	def __init__( self, name, email, empresa):
		Contacto.__init__( self,name, email)
		self.empresa = empresa

	def getEmpresa( self ):
		return self.empresa

	def __str__( self ):
		return str.format("{0} Empresa: {1}\n",
						  Contacto.__str__( self ),
						self.getEmpresa())		


class Agenda:
	def __init__( self ):
		self.agenda = dict()
		
	def insertar( self, person ):
		if isinstance(person,Trabajo):
			self.agenda[person.getName()] = Trabajo.__str__(person)
		elif isinstance(person,Amigo):
			self.agenda[person.getName()] = Amigo.__str__(person)
		print("Se ha insertado con exito "+person.getName())
	
	def buscar( self, name ):
		try:
			return self.agenda[name]
		except:
			print("No se ha encontrado a "+name)
			return -1
	
	def borrar( self, name ):
		try:
			self.buscar(name)
			del self.agenda[name]
			print("se ha borrado con exito")
		except:
			print("Se cancela el borrado")
	
	def listar( self ):
		if len(self.agenda.items()) > 0:
			for k,v in self.agenda.items():
				print("Datos de "+k)
				print(self.buscar(k))
		else:
			print("La agenda esta vacia")
			
class Menu:
	def __init__( self, agenda ):
		self.op = -1
		self.agenda = agenda
		self.showMenu()

	def showMenu( self ):
		print("1.Introducir")
		print("2.Buscar")
		print("3.Borrar")
		print("4.Listar")
		print("5.Salir")
		self.pedirOpcion()

	def pedirOpcion( self ):
		try:
			self.op = int(raw_input("Escoja opcion 1,2,3,4. 5 " +
				                "para cerrar programa\n"))
			self.ejecutarOp()
		except:
			print("Introduce 1,2,3,4 o 5")
			self.showMenu()

	def ejecutarOp( self ):
		if self.op == 1:
			self.insertar()
		elif self.op == 2:
			self.buscar()
		elif self.op == 3:
			self.pedirBuscarBorrar()
		elif self.op == 4:
			agenda.listar()
		elif self.op == 5:
			print("Cerrando programa")
		else:
			self.showMenu() 
	
	def datosComunes( self ):
		name = raw_input("Introduzca nombre de contacto: ")
		email = raw_input("Introduzca email de "+name+':')
		return name, email
	
	def pedirNombre( self ):
		name = raw_input("Introduzca nombre de contacto: ")
		return name
	
	def insertar( self ):
		print("Tipo de contacto")
		tipo = raw_input("Escoja amigo o trabajo: ")
		if tipo == "amigo":
			name, email = self.datosComunes()
			self.agenda.insertar(Amigo(name,email))
		elif tipo == "trabajo":
			name, email = self.datosComunes()
			empresa = raw_input("Introduzca empresa de "+name+': ')
			self.agenda.insertar(Trabajo(name,email,empresa))
		self.showMenu()
		
	def buscar( self ):
		name = self.pedirNombre()
		print(self.agenda.buscar(name))
		self.showMenu()
		
			
		



        
	
			
def main():
	agenda = Agenda()
	'''borrar estas pruebas al poner el menu o dejar
	para empezar con datos, eso si borrar listar y buscar'''
	pepe = Amigo("pepe","p@gmail.com")
	manuel = Trabajo("manuel","m@m.es","manuel@am.es")
	agenda.insertar(pepe)
	agenda.insertar(manuel)
	agenda.listar()
	agenda.buscar("pepe")
	Menu(agenda)
	
	
			
if __name__=="__main__":main()

