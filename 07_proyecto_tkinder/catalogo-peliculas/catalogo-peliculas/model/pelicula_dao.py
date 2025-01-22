from .conexion_db import ConexionDB

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
    
    conexion.cursor.execute(sql)
    conexion.cerrar()
    
def borrar_tabla():
    conexion = ConexionDB()
    
    sql='DROP TABLE peliculas'
    
    conexion.cursor.execute(sql)
    conexion.cerrar()
    
    