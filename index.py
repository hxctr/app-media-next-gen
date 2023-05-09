from flask import Flask,request, render_template
from flask_cors import CORS
import json

#Clase la cual me controla los usuarios
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
            text+="{\"nombre\":"+i.nombre+", \"apellido\":"+i.apellido+", \"username\":"+i.username+"}\n"
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
                return True
        return False



#Clase que posee los atributos de los usuarios
class Users:
    def __init__(self,nombre,apellido,username,password):
        self.nombre=nombre
        self.apellido=apellido
        self.username=username
        self.password=password



app = Flask(__name__)

CORS(app)

control = Control()

@app.route('/')#Ruta por default
def index():
    return render_template('index.html')


@app.route('/getAllUsers')#Ruta para obtener todos los usuarios que han sido registrados
def usuarios():
    return control.getUsers()

@app.route('/addUser',methods=['POST'])#Ruta que sirve para registrar un usuario
def addUser():
    data=request.json
    if control.addUser(data['nombre'],data['apellido'],data['username'],data['password']):
        return '{\"data\":\"El usuario ha sido registrado exitosamente\"}'
    else:
        return '{\"data\": \"El usuario ya existe\"}'

@app.route("/getPassword/<username>", methods=["POST"])#Ruta que sirve para mostrar la contraseña de un usuario
def getPass(username):
    valor = request.json
    return control.getPassword(valor['username'])

@app.route('/getSignIn',
#methods=['POST']
)#Ruta que sirve para iniciar sesion
def getSignIn():
    # data=request.json
    # if data['username'] =='admin' and data['password'] == "admin":
    #     return "{\"data\":\"admin\"}"
    # elif control.getSignIn(data['username'],data['password']):
    #     return "{\"data\":\"true\"}"
    # else:
    #     return "{\"data\":\"false\"}"
    return render_template('login.html')

@app.route('/postLogin', methods=['POST'])    
def postLogin():
    data=request.json
    if data['username'] =='admin' and data['password'] == "admin":
        return "{\"data\":\"admin\"}"
    elif control.getSignIn(data['username'],data['password']):
        return "{\"data\":\"true\"}"
    else:
        return "{\"data\":\"false\"}"


if __name__ == "__main__":
    app.run(port="8000",debug=True)  