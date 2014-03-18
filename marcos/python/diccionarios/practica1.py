class Person :  # para heredar class Person (claseDeLaQueHeredas)
    def __init__(self, name, email) :
        self.name = name
        self.email = email
        
class Friend (Person) :
    def __init__(self, name, email) :
        Person.__init__(self, name, email)
        
class Workaholic (Person) :
    def __init__(self, name, email, workEmail) :
        Person.__init__(self, name, email)    
        self.workEmail = workEmail
        

class
