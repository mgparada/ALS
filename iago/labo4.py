#class with common methods to Amigo and Trabajo
class Contacto:
	def __init__( self, name, email ):
		self.name = name
		self.email = email

	def getName( self ):
		return self.name

	def getEmail( self ):
		return self.email

	def __str__( self ):
		return str.format(" Name: {0}\n Email: {1}\n",
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
		return str.format("{0} Company: {1}\n",
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
		print("Correct inserted "+person.getName())
	
	def buscar( self, name ):
		try:
			return self.agenda[name]
		except:
			print("Not found "+name)
			return None
			
			
	
	def borrar( self, name ):
		try:
			self.buscar(name)
			del self.agenda[name]
			print("Correct deleted")
		except:
			print("Cancel delete")
	
	def listar( self ):
		if len(self.agenda.items()) > 0:
			for k,v in self.agenda.items():
				print("Data of "+k)
				print(self.buscar(k))
		else:
			print("Empty address book")
			
class Menu:
	def __init__( self ):
		self.agenda = Agenda()
		self.showMenu()

	#Menu principal
	def showMenu( self ):
		print("Menu options")
		print("1.Insert")
		print("2.Search")
		print("3.Delete")
		print("4.List")
		print("5.Exit")
		self.pedirOpcion()

	
	def pedirOpcion( self ):
		try:
			self.op = int(raw_input("Input option 1,2,3,4. 5 " +
				                "to finish program\n"))
			self.ejecutarOp()
		except:
			'''print("Input 1,2,3,4 o 5")'''
			self.showMenu()

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
			print("End program")
		else:
			print("You input "+str(self.op)+': wrong option')
			print("Input 1,2,3,4 o 5")
			self.showMenu() 
	
	def datosComunes( self ):
		name = raw_input("Input contact name: ")
		email = raw_input("Input "+name+" email's: ")
		return name, email
	
	def pedirNombre( self ):
		name = raw_input("Input contact name: ")
		return name
	
	def insertar( self ):
		print("Contact type")
		tipo = raw_input("Input friend or work: ")
		if tipo == "friend":
			name, email = self.datosComunes()
			self.agenda.insertar(Amigo(name,email))
		elif tipo == "work":
			name, email = self.datosComunes()
			empresa = raw_input("Input "+name+" company's: ")
			self.agenda.insertar(Trabajo(name,email,empresa))
		else:
			print("You input "+tipo+",expected friend or work")
		self.showMenu()
	
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
	
if __name__=="__main__":main()



