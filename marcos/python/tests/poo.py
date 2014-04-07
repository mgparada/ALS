import math
#Dado en clase de teoria 10-03-2014

'''Programacion orientada a objetos(POO) Python'''

class Punto:
    '''x = 0 seria variable estatica pero su valor no puede ser el de la misma
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
                     and self.getY() < other.getY() )
        else:
            return False
    
#operador >
    def __gt__(self, other):
        if ( isinstance( other, Punto ) ):
            return ( self.getX() > other.getX()
        and self.getY() > other.getY() )
        else:
            return False
    
#operado !=
    def __neq__(self, other):
        if ( isinstance( other, Punto ) ):
            return ( self.getX() != other.getX()
               or self.getY() != other.getY() )
        else:
            return False 


if __name__ == "__main__":
	print(str(Point.getOrg()))





















