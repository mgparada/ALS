__author__ = 'mauro'

class Agenda:
    def __init__(self):
        self.dicContactos = {}

    def anadir(self, contacto):
        self.dicContactos[contacto.getNombre()] = contacto

    def borrar(self, nombre):
        if self.dicContactos.get(nombre) != None:
            del(self.dicContactos[nombre])
            return str.format("Contacto {0} eliminado", nombre)

        return str.format("No existe el contacto {0}", nombre)

    def buscar(self, nombre):
        if self.dicContactos.get(nombre) != None:
            contacto = self.dicContactos.get(nombre)
            return contacto.__str__()

        return str.format("No existe el contacto {0}", nombre)

    def listar(self):
        if self.dicContactos.items() > 0:
            for k in self.dicContactos.keys():
                contacto = self.dicContactos[k]
                print ("\n---------\n")
                print contacto.__str__()
        else:
            print ("\n---------\n")
            print "No hay contactos en la agenda"

        print ("\n---------\n")

class Contact:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def getNombre(self):
        return self.nombre

    def getEmail(self):
        return self.email

    def __str__(self):
        return str.format("Nombre: {0}\nEmail: {1}", self.getNombre(), self.getEmail())

class Amigo(Contact):    def __init__(self, nombre, email):
        Contact.__init__(self, nombre, email)

class Trabajo(Contact):
    def __init__(self, nombre, email, email_empresa):
        Contact.__init__(self, nombre, email)
        self.email_empresa = email_empresa

    def getEmailEmpresa(self):
        return self.email_empresa

    def __str__(self):
        return str.format("{0}\nEmail de la empresa: {1}", Contact.__str__(self), self.getEmailEmpresa())


class Menu:
    agenda = Agenda()

    def __init__(self):
        self.selectOption()

    def camposComunes(self):
        nombre = raw_input("Introduce el nombre del contacto: ")
        email = raw_input("Introduce el email del contacto: ")

        return nombre, email

    def insertarAmigo(self):
        nombre, email = self.camposComunes()
        self.agenda.anadir(Amigo(nombre, email))

    def insertarTrabajo(self):
        nombre, email = self.camposComunes()
        email_empresa = raw_input("Introduce el email de la empresa: ")

        self.agenda.anadir(Trabajo(nombre, email, email_empresa))

    def buscarContacto(self):
        nombre = raw_input("Introduce el nombre del contacto que deseas buscar: ")

        print self.agenda.buscar(nombre)

    def eliminarContacto(self):
        nombre = raw_input("Introduce el nombre del contacto que deseas buscar: ")

        print self.agenda.borrar(nombre)


    def listarContactos(self):
        self.agenda.listar()

    def ejecutarOpcion(self, option):
        if option == 0:
            return

        if option == 1 or option == 2 or option == 3 or option == 4:
            (
                {
                    1: self.menuTipoDeContacto,
                    2: self.buscarContacto,
                    3: self.eliminarContacto,
                    4: self.listarContactos
                }[option]
            )()
        else:
            print(str.format("Ha introducido una opcion incorrecta, {0}", option))


    def ejecutarOpcionContactos(self, option):
        if option == 0:
            return

        if option == 1 or option == 2 :
            (
                {
                    1: self.insertarAmigo,
                    2: self.insertarTrabajo
                }[option]
            )()
        else:
            print(str.format("Ha introducido una opcion incorrecta, {0}", option))

    def menuTipoDeContacto(self):
        opt = 1

        while opt != 0:
            opt = (int)(raw_input(self.mostrarMenuContactos()))
            self.ejecutarOpcionContactos(opt)

    def mostrarMenuContactos(self):
        return "Introduzca la opcion que desee: " \
               "\n 1. Amigo." \
               "\n 2. Trabajo." \
               "\n 0. Cancelar." \
               "\n : "


    def mostrarMenu(self):
        return "Introduzca la opcion que desee: " \
               "\n 1. Nuevo contacto." \
               "\n 2. Buscar contacto." \
               "\n 3. Eliminar contacto." \
               "\n 4. Listar contactos." \
               "\n 0. Salir." \
               "\n : "


    def selectOption(self):
        opt = 1

        while opt != 0:
            opt = (int)(raw_input(self.mostrarMenu()))
            self.ejecutarOpcion(opt)


menu = Menu()
