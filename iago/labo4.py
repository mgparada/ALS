#class metodos comunes a Amigo y Trabajo
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

	#sobreescribe el de Contacto para mostrar tambien la empresa
	def __str__( self ):
		return str.format("{0} Empresa: {1}\n",
						  Contacto.__str__( self ),
						self.getEmpresa())		


class Agenda:
	def __init__( self ):
		self.agenda = dict()
	
	'''se inserta en agenda, clave name y valor ya formateado para usarlo en
	print'''
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
			return None
			
			
	
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
	def __init__( self ):
		self.agenda = Agenda()
		self.showMenu()

	#Menu principal
	def showMenu( self ):
		print("Menu opciones")
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
			'''print("Introduce 1,2,3,4 o 5")'''
			self.showMenu()

	#lleva a cabo la opcion escogida por el usuario
	def ejecutarOp( self ):
		if self.op == 1:
			self.insertar()
		elif self.op == 2:
			self.buscar()
		elif self.op == 3:
			self.borrar()
		elif self.op == 4:
			self.listar()
		elif self.op == 5:
			print("Cerrando programa")
		else:
			print("Introducido "+str(self.op)+': opcion erronea')
			print("Introduce 1,2,3,4 o 5")
			self.showMenu() 
	
	#datos comunes a insertar amigo y trabajo
	def datosComunes( self ):
		name = raw_input("Introduzca nombre de contacto: ")
		email = raw_input("Introduzca email de "+name+':')
		return name, email
	
	#nombre solicitado por buscar y borrar
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
		else:
			print("Introducido "+tipo+",esperado amigo o trabajo")
		self.showMenu()
	
	#si no se encuentra agenda devuelve None
	def buscar( self ):
		name = self.pedirNombre()
		found = self.agenda.buscar(name)
		if found != None:
			print(found)
		self.showMenu()
	
	def borrar( self ):
		name = self.pedirNombre()
		self.agenda.borrar(name)
		self.showMenu()
	
	def listar( self ):
		self.agenda.listar()
		self.showMenu()
	

		
def main():
	Menu()
	
	
#para ejecutar main() al pulsar Run		
if __name__=="__main__":main()



