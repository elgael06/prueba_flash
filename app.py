from flask import Flask,render_template,request,redirect,url_for,send_from_directory,json
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os

from api.usuarios import views

app = Flask(__name__,template_folder='frontend/build/',static_folder='static/')
CORS(app)

"""
API`S

"""
@app.route('/api/getUsuarios/')
def getUsuarios():
    print('api usuarios')
    return json.dumps(views.usuarios())

@app.route('/api/addUsuarios/',methods=['POST'])
def add_usuario():
    try:
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
        return json.dumps({"message":"usuario guardado..."})
    except Exception as e:
        return json.dumps({"message":str(e)})

'''
    URL DINAMICA
'''
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def Home_app(path):
    '''paguina principal. '''
    print('path ',path)
    if path != "" and os.path.exists(app.template_folder + '/' + path):
        return send_from_directory(app.template_folder, path)
    
    elif path != "" and os.path.exists(app.static_folder + '/' + path):
        print('index')
        return send_from_directory(app.static_folder, path)
    
    else:
        return send_from_directory(app.template_folder,'index.html')
    # return render_template('index.html')

if __name__ == "__main__":    app.run(debug=True,port=8080,use_reloader=True, threaded=True)