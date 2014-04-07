from __future__ import print_function
import sys

def getEmailByName(name, myDic):
        if myDic.get(name) != None:
                return myDic.get(name)
        
        return -1

def listado(myDic):
        for k, v in myDic.items():
                print ( "---" )
                print (str.format("Nombre: {0} \nEmail: {1}", k, v) )

def introducir(myDic):
        try:
                nombre = raw_input("Introduce el nombre : ")
                email = raw_input("Introduce el email : ")
                
                guardar = 1
                if myDic.get(nombre) != None:
                        guardar = 0
                        
                myDic[nombre] = email
                
                if guardar == 1:
                        print ("Los datos se han guardado correctamente")
                else:
                        print ("Los datos se han editado correctamente")
        except:
                print ("No se han podido guardar los datos")
        
        
def borrar(myDic):
        try:
                nombre = raw_input("Introduce el nombre : ")
                
                del myDic[nombre]
                
                print ("Los datos se han borrado correctamente")
        except:
                print ("Los datos no existen")
        
def buscar(myDic):
                nombre = raw_input("Introduce el nombre : ")
                email = getEmailByName(nombre, myDic)
                
                if not isinstance(email, int) :
                        print ("Nombre : " + nombre)
                        print ("Email : " + email)
                else:
                        ## Imprimir mensajes en stderr !!
                        print ("El usuario no existe", file=sys.stderr)
                        return -1
                

def doAction(opt,myDic): 
        options = {
                1: introducir,
                2: borrar,
                3: buscar,
                4: listado,
        }      
        result = options[int(opt)](myDic)
        
def menu():
        print ("--- Menu ---")
        print ("Pulse el numero de la opcion: ")
        print ("1. Introducir")
        print ("2. Borrar")
        print ("3. Buscar")
        print ("4. Listar")
        print ("0. Salir")
        
def main():
        opt = 10
        myDic = {}
        while int(opt) != 0:
                menu()
                opt = int(raw_input("Introduce una opcion: "))
                if opt != 0:
                        doAction(opt, myDic)
                
        print ("Hasta otra!!")
        
main()