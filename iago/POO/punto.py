class Punto:
    @staticmethod
    def getOrg():
        return Punto(0,0)
    def __init__(self, a, b):
        z = 0 # Creando una variable local
        self.x = a # Creando atributo
        self.y = b
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def __gt__(self, other):
        if (isinstance(other, Punto)):
            return(self.getX()>other.getX()
                   or self.getY() > other.getY())
        else:
            return False
    
    def __lt__(self,other):
        if (isinstance(other,Punto)):
            return(self.getX() < other.getX()
                   or self.getY() < other.getY())
        else:
            return False
    
    
    def __eq__(self, other):
        if (isinstance(other, Punto)):
            return(self.getX()== other.getX()
                   and self.getY() == other.getY() )
    
    def __str__(self):
        return str.format("({0},{1})",
                          self.getX(),
                          self.getY() )
    
if __name__=="__main__":
    print(Punto.getOrg())