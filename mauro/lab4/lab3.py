__author__ = 'mauro'


def insertar():
    nombre = raw_input("Introduce el nombre del contacto: ")
    email = raw_input("Introduce el email del contacto: ")

    dic[nombre] = email

def buscar():
    nombre = raw_input("Introduce el nombre del contacto: ")

    if dic.get(nombre) != None:
        print(str.format("Nombre: {0}\nEmail: {1}", nombre, dic.get(nombre)))
    else:
        print(str.format("El usuario {0} no existe", nombre))

def borrar():
    nombre = raw_input("Introduce el nombre del contacto: ")

    if dic.get(nombre) != None:
        del(dic[nombre])
    else:
        print(str.format("El usuario {0} no existe", nombre))


def listar():
    for k, value in dic.items():
        print ("\n-----------\n")
        print( str.format("Nombre: {0}\nEmail: {1}", str(k), str(value)) )

    print ("\n-----------\n")

def menu():
    opt = 1

    str_menu = "\nIntroduce la opcion:" \
               "\n 1. Insertar." \
               "\n 2. Buscar." \
               "\n 3. Borrar." \
               "\n 4. Listar" \
               "\n 0. Salir" \
               "\n : "

    while opt != 0:
        opt = int(raw_input(str_menu))
        if opt != 0:
            (
                {
                    1: insertar,
                    2: buscar,
                    3: borrar,
                    4: listar
                }[opt]
            )()


dic = {}
menu()