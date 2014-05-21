#http://webs.uvigo.es/jbgarcia/prys/pooi/

## Interprete:
# - Crear y eliminar objetos
# - anhadir/modificar y eliminar atributos
# - anhadir/modificar y eliminar metodos

def mainMenu():
    print(" - 1. Crear un nuevo objeto.")
    print(" - 2. Eliminar un objeto existente.")
    print(" - 3. Anhadir o modificar un atributo.")
    print(" - 4. Eliminar un atributo.")
    print(" - 5. Anhadir o modificar un metodo.")
    print(" - 6. Eliminar un metodo.")
    in = raw_input("Elija una opcion: ")
    
    return in

def Interpreter:
    def createObject(className):
        toExecute = str.format("o = {1}()", className);
        exec(toExecute)
        print("Creado objeto " + o + "de la clase " + className);
    def removeObject(objectName):
        del objectName
        print("Eliminado objeto " + objectName + ".");        
    def setAttribute(obj, attr, value):
        obj.attr = value
    def removeAttribute(obj, attr, value):
        
    
        