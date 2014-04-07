__author__ = 'mauro'


class Agenda:
    def __init__(self):
        self.listaContactos = {}

    def nuevo(self, Contacto):
        self.listaContactos[Contacto.nombre] = Contacto;

    def borrar(self, nombre):
        del (self.listaContactos[nombre])

    def getContacto(self, nombre):
        return self.listaContactos.get(nombre);

    def listar(self):
        print("\n")

        for k in self.listaContactos.keys():
            print( str.format("----------\n{0}", self.listaContactos[k].toString() ) )

        print("----------\n")


class Contacto:
    def __init__(self, nombre, email):
        self.nombre = nombre;
        self.email = email;

    def getEmail(self):
        return self.email;

    def setEmail(self, email):
        self.email = email;

    def getNombre(self):
        return self.nombre;

    def setNombre(self, nombre):
        self.nombre = nombre;

    def toString(self):
        return str.format("Nombre {0}\nEmail {1}", self.getNombre(), self.getEmail());


class Amigo(Contacto):
    def __init__(self, nombre, email):
        Contacto.__init__(self, nombre, email)


class Trabajo(Contacto):
    def __init__(self, nombre, email, email_empresa):
        self.email_empresa = email_empresa;
        Contacto.__init__(self, nombre, email);

    def getEmailEmpresa(self):
        return self.email_empresa;

    def toString(self):
        return str.format("{0} \nEmail de la empresa {1}",
                          Contacto.toString(self), self.getEmailEmpresa());


def contactoAmigo():
    nombre = raw_input("Introduce el nombre del contacto: ")
    email = raw_input("Introduce el email del contacto: ")

    contacto = Amigo(nombre, email)

    agenda.nuevo(contacto)

def contactoTrabajo():
    nombre = raw_input("Introduce el nombre del contacto: ")
    email = raw_input("Introduce el email del contacto: ")
    email_empresa = raw_input("Introduce el email de la empresa del contacto:")

    contacto = Trabajo(nombre, email, email_empresa)

    agenda.nuevo(contacto)

def nuevoContacto():
    opt = 1

    while opt > 0:
        opt = int(raw_input("Introduce el tipo de contacto: "
                            "\n 1. Amigo."
                            "\n 2. Trabajo"
                            "\n 0. Salir."
        ))

        if opt != 0:
            (
                {
                    1: contactoAmigo,
                    2: contactoTrabajo
                }[opt]
            )()

def listarContactos():
    agenda.listar()

def buscarContacto():
    nombre = raw_input("Introduce el nombre del contacto: ")
    contacto = agenda.getContacto(nombre)

    print ("\n-------\n")
    print contacto.toString()
    print ("\n-------\n")

def borrarContacto():
    nombre = raw_input("Introduce el nombre del contacto: ")

    agenda.borrar(nombre)

    listarContactos()

def menu():
    opt = 1;

    str_menu = "Introduce la opcion: " \
           "\n 1.Nuevo contacto." \
           "\n 2.Listar Contactos." \
           "\n 3.Buscar Contacto." \
           "\n 4.Borrar Contacto." \
           "\n 0.Salir." \
           "\n : "

    while opt > 0:
        opt = int(raw_input(str_menu))

        if opt != 0:
            (
                {
                    1:nuevoContacto,
                    2:listarContactos,
                    3:buscarContacto,
                    4:borrarContacto
                }
                [opt]
            )()


agenda = Agenda()
menu()