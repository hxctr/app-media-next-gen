class Users:
    def __init__(self,nombre,apellido,username,password):
        self.nombre=nombre
        self.apellido=apellido
        self.username=username
        self.password=password

class Control:
    def __init__(self):
        self.users=[]
    
    def addUser(self,nombre,apellido,username,password):#Metodo que registra un usuario
        newUser = Users(nombre,apellido,username,password)
        if self.existUser(username):
            return False
        else:
            self.users.append(newUser)
            return True

    def existUser(self,username):#Metodo que verifica si el usuario registrado ya existe
        for i in self.users:
            if i.username==username:
                return True
        return False

    def getUsers(self):#Metodo que devulve los usuarios registrados
        text="[\n"
        for i in self.users:
            text+="{\"nombre\":\""+i.nombre+"\", \"apellido\":\""+i.apellido+"\", \"username\":\""+i.username+"\"}\n,"
        text = text[:-1]
        text+='\n]'
        return text

    def getPassword(self, username):#Metodo que devuelve la contraseña de un usuario
        for i in self.users:
            if i.username == username:
                return "{\"password\":\""+i.password+"\"}\n"
        return ""

    def getSignIn(self,username,password):#Metodo para iniciar sesion
        for i in self.users:
            if i.username==username and i.password==password:
                print(i.username)
                return True, i.username
        return False


