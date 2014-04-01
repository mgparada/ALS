import math
#Dado en clase de teoria 10-03-2014

'''Programacion orientada a objetos(POO) Python'''

class Punto:
    '''x = 0 seria variable estatica pero su valor  no puede ser el de la misma
    clase a la que pertenece'''
    #x = Punto(0,0) no podria ser por lo dicho antes
    
    #metodo estatico python 2
    @staticmethod
    def getOrg():
        return Punto( 0, 0 )
    
    '''Constructor se llama init, por convencion se llama self al param recibido,
    obligatorio pasarlo en la clase no se pasa en las llamadas'''
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    #equivalente a metodo toString
    def __str__(self):
        return str.format( "({0}, {1})", 
                           self.getX(), 
                           self.getY() )
    
    #opeador ==, euivalente a equals
    def __eq__(self, other):
        if ( isinstance( other, Punto ) ):
            return ( self.getX() == other.getX()
                     and self.getY() == other.getY() )
        else:
            return False
    
	#operador <
    def __lt__(self, other):
        if ( isinstance( other, Punto ) ):
            return ( self.getX() < other.getX()
                     or self.getY() < other.getY() )
        else:
            return False 
    
	#operador >
    def __gt__(self, other):
        if ( isinstance( other, Punto ) ):
            return ( self.getX() > other.getX()
        or  self.getY() > other.getY() )
        else:
            return False 
    
	#operado !=
    def __neq__(self, other):
        if ( isinstance( other, Punto ) ):
            return ( self.getX() != other.getX()
               or  self.getY() != other.getY() )
        else:
            return False 
    
        
        
'''Pruebas para la clase Punto'''
p1 = Punto(5, 4)
p2 = Punto(5, 4)
p3 = Punto(6, 7)
p4 = Punto(0,0)

#prueba eq
p1 == p2
#prueba gt
p1 > p3
#prueba lt
p4 < p1
#prueba neq
p1 != p4

class Linea:
    def __init__(self, p1, p2):
        self.begin = p1
        self.end = p2
        
    def getStart(self):
        return self.begin
    
    def getEnd(self):
        return self.end
    
    def __str__(self):
        return str.format( "( {0} - {1} )",
                           str( self.getStart() ),
                           str( self.getEnd() ))
    


#pruebas class Linea
l = Linea(1,2)
print(l)
   
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email
    
    def __str__(self):
        return str.format( "{0} {1}",
                           self.getName(),
                           self.getEmail() )

#Class con herencia, en este caso de Person    
class Employee(Person):
    def __init__(self, name, email, firm):
        Person.__init__( self, name, email )
        self.firm = firm
        
    def getFirm(self):
        return self.firm
    
    def __str__(self):
        return str.format( "{0} @ {1}",
                           Person.__str__( self ),
                           self.getFirm() )

#prueba class Employee
em = Employee("manolo","pepe@pepe.com","pepe")
print(em)

'''Ejercicio:
El usuario escoge círculo o rectangulo,
se le piden los datos para crearlo y se muestran esos datos y
el area calculada

Crear Class
class Circulo
class Rectangulo
Metodos minimo a crear en las class

def __str__
def calculaArea
'''
#Fin enunciado ejercicio----------------------
class Circulo:
    def __init__(self,radio):
        self.radio = radio
        
    def getRadio(self):
        return float(self.radio)
    
    def calculaArea(self):
        return math.pi * (self.getRadio() ** 2)
    
    
    def __str__(self):
        return str.format("El radio del circulo es {0}",
                          self.getRadio() )
    
class Rectangulo:
    def __init__(self,base,alto):
        self.base = base
        self.alto = alto
    
    def getBase(self):
        return float(self.base)
    
    def getAlto(self):
        return float(self.alto)
        
    def calculaArea(self):
        return self.getBase() * self.getAlto()
    
    def __str__(self):
        return str.format( "Base es {0}, alto es {1}",
                           self.getBase(),
                           self.getAlto() )
    
def ejerFig():
    op = raw_input("introduce circulo o rectangulo: ")
    if op == "circulo":
        data = raw_input("introduce radio: ")
        fig = Circulo(data)
        print(fig)
        print(fig.calculaArea())
    elif op == "rectangulo":
        base = raw_input("introduce base: ")
        alto = raw_input("introduce alto: ")
        fig = Rectangulo(base,alto)
        print(fig)
        print(fig.calculaArea())
    else:
        print("introducido {0} : esperado circulo o rectangulo".format(op))
    
 #Fin Ejercicio figura -------------------------------       
        
