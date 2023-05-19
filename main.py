from flask import Flask,request, render_template, session, redirect, url_for, jsonify
from flask_session import Session
from flask_cors import CORS
from post import Newsletter
from user import Control
import json

app = Flask(__name__)

CORS(app)
Session(app)

sess = Session()
control = Control()
newsletter = Newsletter()

app.config['SECRET_KEY'] = 'g5h2s7g6f5g4'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '/dev/null'


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
        return '{\"data\":\"Your account has been created\"}'
    else:
        return '{\"data\": \"User already exists\"}'

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
    

