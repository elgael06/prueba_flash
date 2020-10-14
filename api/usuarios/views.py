from datetime import datetime

lista_usuarios = [
    {
        'id':1,
        'nombre':'gael',
        'apeido':'valenz',
        'create':'10-10-2020',
        'img':'',
    }
]

def usuarios():
    lista =[]
    
    for item in lista_usuarios:
        lista.append({
            'id':str( item['id'] ),
            'nombre':item['nombre'],
            'apeido':item['apeido'],
            'fecha_alta':item['create'],
            'img':item['img'],
        })
    
    return lista

def insertar(nombre,apeido,image):
    fecha = datetime.now()
    id = len( lista_usuarios)+1
    print(id,nombre,apeido,image)
    lista_usuarios.append({
        'id':id,
        'nombre':nombre,
        'apeido':apeido,
        'create':fecha.strftime('%d-%m-%y %H:%M:%S'),
        'img':image,
    })