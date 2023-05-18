from flask import Flask,request, render_template, session, redirect, url_for, jsonify
from flask_cors import CORS
from flask_session import Session
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
                print(i.username)
                return True, i.username
        return False

class Newsletter:
    def __init__(self):
        self.news = []
    # I will do the methods here to insert news
    def addPost(self, username, headline, body):
        newPost = News(username, headline, body)
        self.news.append(newPost)

    def getPosts(self):
        

        if len(self.news) > 0:
            text = '['
            #yes there posts
            for i in self.news:
                text += "\n{\"username\":\""+i.username+"\",\n\"headline\":\""+i.headline+"\",\n\"body_post\":\""+i.body+"\"},"
            text = text[:-1]
            text+='\n]'
            print(len(text))
            return text
        
        else:
            

            text='[\n]'
            # print(len(text))
            #length of 3
            return text
       

       
        
        

       
        



#Clase que posee los atributos de los usuarios
class Users:
    def __init__(self,nombre,apellido,username,password):
        self.nombre=nombre
        self.apellido=apellido
        self.username=username
        self.password=password

class News:
    def __init__(self, username, headline, body):
        self.username = username
        self.headline = headline
        self.body = body
    
    





app = Flask(__name__)

CORS(app)
Session(app)

control = Control()
newsletter = Newsletter()

app.config['SECRET_KEY'] = 'clave_secreta'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '/dev/null'
sess = Session()


@app.route('/')#Ruta por default
def index():
    return render_template('index.html')

@app.route('/normalUser')
def normalUser():
    return render_template('normalUser.html')

@app.route('/getAllUsers')#Ruta para obtener todos los usuarios que han sido registrados
def usuarios():
    return control.getUsers()

@app.route('/getAllPosts')#I have to use this function to get all post in the dashbord, but with no pressing something, just adding a request from the fetch
def getAllPosts():
    return newsletter.getPosts()

@app.route('/addUser',methods=['POST'])#Ruta que sirve para registrar un usuario
def addUser():
    data=request.json
    if control.addUser(data['nombre'],data['apellido'],data['username'],data['password']):
        return '{\"data\":\"El usuario ha sido registrado exitosamente\"}'
    else:
        return '{\"data\": \"El usuario ya existe\"}'

@app.route('/add_post', methods=["POST"])
def add_post():
    data = request.json #this line reads the json send in postman, and acts like a dict 
    newsletter.addPost(data['username'], data['headline'], data['body_post'])
    return "{\"data\":\"Data posted successfully\"}"

    

@app.route('/registerView')
def registerView():
    return render_template('register.html')

@app.route("/getPassword/<username>", methods=["POST"])#Ruta que sirve para mostrar la contraseña de un usuario
def getPass(username):
    valor = request.json
    return control.getPassword(valor['username'])


@app.route('/recoveryPass')
def recoveryPass():
    return render_template('resetPass.html')

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
    global userg
    userg = ''
    

    if data['username'] =='admin' and data['password'] == "admin":
        return "{\"data\":\"admin\"}"
    elif control.getSignIn(data['username'],data['password']):
        # boolResponse, current_user = control.getSignIn(data['username'],data['password'])
        boolResponse, userg = control.getSignIn(data['username'],data['password'])
        # session['usuario_actual'] = current_user
        print('-----'+userg)
        return "{\"data\":\"true\", \"username\":\""+userg+"\"}"
    else:
        return "{\"data\":\"false\"}"


@app.route('/admin')
def admin():
    return render_template('admin.html', usuario = 'Administrator')

@app.route('/dashboard')
def dashboard():
    usuario_actual = session.get('usuario_actual')
    return render_template('dashboard.html', usuariol = userg)

@app.route('/post')
def post():
    return render_template('post.html', usuariol = userg)


@app.route('/logout')
def logout():
    session.pop('usuario_actual', None)
    return redirect(url_for('index'))



if __name__ == "__main__":
    
    sess.init_app(app)
    app.run(port="5000",debug=True)  
    

