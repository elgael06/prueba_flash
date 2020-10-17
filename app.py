from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os

from api.usuarios import views

app = Flask(__name__)

@app.route('/')
def Home_app():
    '''paguina principal. '''
    return render_template('/index.html',name='gael')

@app.route('/usuarios')
def obter_usuarios():
    '''muestas todos los usarios en una lista.'''
    return render_template('/usuarios/index.html',lista=views.usuarios())

@app.route('/crear',methods=['GET','POST'])
def crear_usuario():
    '''formulario para crear usuario '''
    print(request.method)
    if(request.method=='GET'):
        return render_template('usuarios/crear.html')
    elif request.method=='POST':
        #datos de formulario
        nombre      = request.form['nombre']
        apeido      = request.form['apeido']
        #archivo en formulario.
        imagen      = request.files['avatar']
        #url donde se guardara arcivo
        url_image   = 'static/images/avatar/' + nombre + '_'+ apeido+'_' + secure_filename(imagen.filename)
        #guardamos archivo
        imagen.save(url_image)
        #agregamos archivo a lista
        views.insertar(nombre=nombre,apeido=apeido,image=url_image)
        #redirigimos a url de usuarios
        return redirect(url_for('obter_usuarios'))#llama al metodo obtener usuarios

if __name__ == "__main__":
    # app.static_folder('')
    # app.template_folder('')
    app.run(debug=True,port=8080)