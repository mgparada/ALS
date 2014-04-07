#EJERCICIO 4

class Punto:
	def __init__(self,x,y):
		self.__x=x;
		self.__y=y;
	def getX(self):
		return self.__x;
	def getY(self):
		return self.__y;
	def __str__(self):
		return str.format("({0},{1})",self.getX(),self.getY());
		
class Linea:
	def __init__(self,p1,p2):
		self.__p1=p1;
		self.__p2=p2;
	def getInic(self):
		return self.__p1;
	def getFin(self):
		return self.__p2;
	def __str__(self):
		return str.format("{0}-{1}",self.getInic() , self.getFin());
	
class Poligono:
	def __init__(self, lista):
		self.__lineas=[];
		tam = len(lista);
		if(tam<2):
			print("debes meter 3 puntos al menos");
		else:
			i=0;
			while (i<tam):
				if(i==tam-1):
					self.__lineas.append(Linea(lista[i],lista[0]))
				else:
					self.__lineas.append(Linea(lista[i],lista[i+1]))
				i+=1;
	def getLineas(self):
		return self.__lineas;
	def __str__(self):
		ret = "{";
		lista = self.getLineas();
		tam = len(lista);
		i=0;
		while (i<tam):
			if(i==tam-1):
				ret+=str(lista[i]);
			else:
				ret+=str(lista[i])+" , ";
			i+=1;
		ret+="}";
		return ret;
			
p = Punto(1,2);
print("Punto: "+str(p));
p2 = Punto(3,4);
l = Linea(p,p2);
print("Linea: "+str(l));
p3 = Punto(4,1);
listaa=[p,p2,p3];
poli = Poligono(listaa);
print("Poligono: " + str(poli));
