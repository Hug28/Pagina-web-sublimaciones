from flask import Flask,redirect,render_template,url_for,jsonify,request,flash
from flask_login import LoginManager,login_required,logout_user,login_user
from flask_wtf.csrf import CSRFProtect
from db.db import get_conn
from werkzeug.utils import secure_filename
import os
import uuid 

from models.ModelUser import ModelUser
from models.User import User
from models.Metodos import Metodos


app=Flask(__name__)
app.secret_key=os.environ.get("SECRET_KEY")


csrf=CSRFProtect(app)
db=get_conn()
login_manager=LoginManager(app)


@login_manager.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html")


#RUTAS DE PRODUCTOS:
@app.route("/seccion/<seccion_name>")
def seccion(seccion_name):
    opcion=seccion_name.lower()
    resu=Metodos.select(db,opcion)
    
    if(resu is not None):
        return render_template("productos.html",resu=resu)
    return render_template("productos.html",msj="error")

    

#LOGIN
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form["name"]
        password=request.form["password"]

        user=User(0,name,password)
        logges_user=ModelUser.login(get_conn(),user)

        if logges_user !=None:
            if logges_user.password:
                login_user(logges_user)
                return redirect(url_for("admin"))
            else:
                flash("Datos incorrecto")
                return redirect(url_for("login"))
        else:
            flash("Datos incorrectos")
            return redirect(url_for("login"))
    else:
        return render_template("auth/login.html")

@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")

#Logout
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


#Agregar producto
@app.route("/agregar",methods=["GE","POST"])
def agregar():
    if request.method=="POST":
        categoria=request.form["producto"]
        img=request.files["img"]
        if (img.filename):
           new_img=nombre_de_img(img,categoria)
           Metodos.insert(db,new_img)
        return redirect(url_for("admin"))



#GUARDAR IMAGEN Y RETORNAR EL NOMBRE PARA GUARDAR EN BASE DE DATOS
def nombre_de_img(img,dato):
    basepath=os.path.dirname(__file__)
    filename=secure_filename(img.filename)
    id=str(uuid.uuid4())
    name=dato+id+filename
    upload_path=os.path.join(basepath,'static/asset/img',name)
    img.save(upload_path)
    return name





def status_401(error):
    return redirect(url_for("login"))

def status_404(error):
    return "<h1>ERROR</h1>"

if __name__=='__main__':
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run(debug=True)
