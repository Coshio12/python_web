"""
    En el siguiente codigo veremos como interactuan los archivos python y mandar la informacion
    a una plantilla de html
    
    Para ello debemos crear una carpeta template, donde estaran todas las vistas
    Para los archivos estaticos como imagenes, js, videos, etc. debemos guardarlos en una carpeta
    llamada static y podemos ordenarlo con las carpetas img, js, etc.
"""
#Importamos Flask y render template desde flask
from flask import Flask, render_template

#Creacion el objeto de Flask
app = Flask(__name__)

#Desde el pbjeto app creamos las rutas de nuestra pagina
@app.route('/')
@app.route('/hola')

#Creamos la funcion hola
def hola():
    #Creamos la variable mensaje
    mensaje = 'Hola mundo con Flask'
    #return '<h2>Hola Mundo de Flask</h2>'
    
    #En un return retornamos el render_template que recibe como parametros el archivo html y mensaje que queremos mandar
    return render_template('index.html',msm = mensaje)

#Creamos una clase blog
class Blog:
    #Creamos el constructor con dos variables
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion

#Creamos la ruta
@app.route('/blogs')

#Creamos una funcion blog donde se creara el objeto con la informacion de la clase Blog
def blog():
    b1 = Blog(
        '¿Que es python',
        'Descripcion de blogs 1'
    )
    
    b2 = Blog(
        '¿Que es flask?',
        'Descripcion de blogs 2'
    )
    
    #Lo guardamos en una lista los dos objetos creados
    blogs = [b1,b2]
    
    #Retornamos a la vista blog.html la lista de blogs
    return render_template('blog.html' , blogs = blogs)

#Creamos las rutas
@app.route('/saludar')

#Si queremos mandar informacion por url tenemos que encerrar la variable dentro los signos de mayor y menor
@app.route('/saludar/<nombre>')
@app.route('/saludar/<nombre>/<edad>')

#Creamos la funcion saludar
#Y las variables que queremos usar desde la url tenemos que darle un valor inicion de None para que no devuelva un TypeError
def saludar(nombre = None, edad = None):
    #Mandamos la informacioon a las vistas html con las variables que recibiremos desde la url
    return render_template('hola.html',nombre = nombre, edad = edad)

#Iniciamos el servidor del entorno virtual
if __name__ == '__main__':
    app.run(debug=True)
    
"""
    Una vez creado todas las funciones iremos a modificar los archivos html para recibir y mandar la informacion
    y poder mostrarlo dentro de una pagina web
"""