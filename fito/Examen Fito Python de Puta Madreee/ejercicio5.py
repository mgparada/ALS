#EJERCICIO 5

class Estudiante:
	def __init__(self,dni,nombre,email):
		self.__dni=dni;
		self.__nombre=nombre;
		self.__email=email;
	def getDni(self):
		return self.__dni;
	def getNombre(self):
		return self.__nombre;
	def getEmail(self):
		return self.__email;
	def __str__(self):
		return str.format("dni: {0}\nnombre: {1}\nemail: {2}",self.getDni(),self.getNombre(),self.getEmail());
		
class EstudianteNormal(Estudiante):
	def __init__(self,dni,nombre,email,provincia):
		Estudiante.__init__(self,dni,nombre,email);
		self.__provincia=provincia;
	def getProvincia(self):
		return self.__provincia;
	def __str__(self):
		return str.format("{0}\nprovincia: {1}\n\n",Estudiante.__str__(self),self.getProvincia());
		
class EstudianteErasmus(Estudiante):
	def __init__(self,dni,nombre,email,paisOrigen):
		Estudiante.__init__(self,dni,nombre,email);
		self.__paisOrigen=paisOrigen;
	def getPaisOrigen(self):
		return self.__paisOrigen;
	def __str__(self):
		return str.format("{0}\npais de origen: {1}\n\n",Estudiante.__str__(self),self.getPaisOrigen());

yop=EstudianteNormal("11111111V","Adolfo","fito1001@gmail.com","Galicia");
print(str(yop));
yop2=EstudianteErasmus("11111111V","Adolfo","fito1001@gmail.com","Portugal");
print(str(yop2));
