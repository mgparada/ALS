def menuPrincipal() :
    opt = int(-1)
    
    while (opt < 0 or opt > 4) :
        print ("1.- Introducir")
        print ("2.- Borrar")
        print ("3.- Buscar")
        print ("4.- Listar")
        print ("0.- Salir")
        opt = int(raw_input("Elige un valor: "))
        
        if (opt != 1 and opt != 2 and opt and opt != 4 and opt != 0) :
            print ("Opcion incorrecta. Elija otra.")
    
    return opt

def menuIntroducirDatos(data) :
    name = raw_input ("Introduce nombre: ")
    data[name] = raw_input ("Introduce mail: ")

    return data    

def recuperarNombre() :
    name = raw_input("Introduce nombre: ")
    
    return name

def borrarDatos(name, data) :
    if (data.get(name) != None) :
        data.pop(name)
    else :
        print ("Imposible borrar datos");
    
def buscar(toSearch, data) :
    if (data.get(toSearch) != None) :
        print(data.get(toSearch))
    else :
        print("No se ha encontrado buscado.")
    

def listado(data) :
    for key, value in data.items() :
        print(str.format("Nombre: {0}\nCorreo: {1}\n\n", key, value))
    
    
def seleccionaOpcion(opt, data) :
    if (opt == 1) :
        menuIntroducirDatos(data)
        print(data)
    elif (opt == 2) :
        toDelete = recuperarNombre()
        borrarDatos(toDelete, data)
    elif(opt == 3) :
        toSearch = recuperarNombre()
        buscar(toSearch, data)
    elif(opt == 4) :
        listado(data)
    else :
        print ("Saliendo del programa...")

    
if (__name__ == "__main__") :
    data = dict()
    opt = int(-1)
    while (opt != 0) :
        opt = menuPrincipal()
        seleccionaOpcion(opt, data)