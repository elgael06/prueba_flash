from flask import Flask,render_template,request,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename
import os

from api.usuarios import views

app = Flask(__name__,static_folder='frontend/build/',template_folder='frontend/build/')


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

'''
    URL DINAMICA
'''
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def Home_app(path):
    '''paguina principal. '''
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.template_folder,'index.html')

if __name__ == "__main__":
    app.run(debug=True,port=8080)