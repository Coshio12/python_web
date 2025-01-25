import os
import sys
import sqlite3


def resource_path(relative_path):
    """Obtiene la ruta absoluta de un archivo, compatible con ejecutables."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class ConexionDB:
    def __init__(self):
        self.base_datos = resource_path('database/peliculas.db')
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
        