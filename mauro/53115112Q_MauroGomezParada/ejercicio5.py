__author__ = 'mauro'

# Ejercicio 5

class Estudiante:
    def __init__(self, nombre, email, dni):
        self.nombre = nombre
        self.email = email
        self.dni = dni

    def getNombre(self):
        return self.nombre

    def getDni(self):
        return self.dni

    def getEmail(self):
        return self.email

    def __str__(self):
        return str.format("\n Nombre: {0}\n Dni: {1}\n Email: {2}", self.getNombre(), self.getEmail(), self.getDni())


class EstudianteNormal(Estudiante):
    def __init__(self, nombre, email, dni, provincia):
        Estudiante.__init__(self,nombre, email, dni)
        self.provincia = provincia

    def getProvincia(self):
        return self.provincia


    def __str__(self):
        return str.format("{0}\n Provincia: {1}", Estudiante.__str__(self), self.getProvincia() )


class EstudianteErasmus(Estudiante):
    def __init__(self, nombre, email, dni, pais):
        Estudiante.__init__(self, nombre, email, dni)
        self.pais = pais

    def getPais(self):
        return self.pais

    def __str__(self):
            return str.format("{0}\n Pais: {1}", Estudiante.__str__(self), self.getPais() )

print ("--- Ejercicio 5 ---")

e1 = EstudianteNormal("Mauro", "mgparada@esei.uvigo.es", "55555555A", "Ourense")
print("Estudiante normal: " + str(e1))

e2 = EstudianteErasmus("Aasfas", "asfas@asdaf.com", "45232311242W", "Letonia")
print("Estudiante erasmus: " + str(e2) )