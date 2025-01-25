from .conexion_db import ConexionDB
from tkinter import messagebox as mg

def crear_tabla():
    conexion = ConexionDB()
    
    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre_pelicula VARCHAR(150),
        duracion_pelicula VARCHAR(150),
        genero_pelicula VARCHAR(150),
        
        PRIMARY KEY (id_pelicula AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        mg.showinfo(titulo,mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        mg.showwarning(titulo,mensaje)
    
def borrar_tabla():
    conexion = ConexionDB()
    
    sql='DROP TABLE peliculas'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se borro con exito'
        mg.showinfo(titulo,mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        mg.showinfo(titulo,mensaje)
        
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        
    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'
    
def guardar(pelicula):
    conexion = ConexionDB()
    sql=f'''
        INSERT INTO peliculas (nombre_pelicula,duracion_pelicula,genero_pelicula)
        values('{pelicula.nombre}','{pelicula.duracion}', '{pelicula.genero}')
    '''
    try:
        conexion.cursor.execute(sql)
        titulo = 'BASE DE DATOS'
        mensaje = 'Se ha guardado el registro'
        mg.showinfo(titulo,mensaje)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla peliculas no esta creada en la base de datos'
        mg.showerror(titulo,mensaje)

def listar():
    conexion = ConexionDB()
    
    lista_peliculas = []
    
    sql='SELECT * FROM peliculas'
    
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la base de datos'
        mg.showerror(titulo,mensaje)
    return lista_peliculas

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    sql= f'''
        UPDATE peliculas
        SET nombre_pelicula = '{pelicula.nombre}',
        duracion_pelicula = '{pelicula.duracion}',
        genero_pelicula = '{pelicula.genero}'
        WHERE id_pelicula = {id_pelicula}
    '''
    
    try:
        conexion.cursor.execute(sql)
        titulo = 'BASE DE DATOS'
        mensaje = 'Se ha editado el registro'
        mg.showinfo(titulo,mensaje)
        conexion.cerrar()
    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se ha podido editar este registro'
        mg.showerror(titulo,mensaje)
        
def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql =f'''
        DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}
    '''
    
    try:
        conexion.cursor.execute(sql)
        titulo = 'BASE DE DATOS'
        mensaje = 'Se ha borrado el registro'
        mg.showinfo(titulo, mensaje)
        conexion.cerrar()
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se ha podido eliminar este registro'
        mg.showerror(titulo, mensaje)