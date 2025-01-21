"""
    Ahora con todo lo que aprendimos vamos a crear nuestra aplicacion con una
    interfaz de usuario mas amigable
    
    Para ello usaremos tkinder
"""
#Importamos tkinder con un alias
import tkinter as tk

#Importamos una clase que esta en la carpeta client y haciendo referencia al archivo deseado y importamos el metodo frame
from client.gui_app import Frame, barra_menu

#Creamos la funcion main
def main():
    #creamos un objeto de tkinder con Tk() que generara una ventana
    root = tk.Tk()
    #Cambiamos el titulo
    root.title('Catalogo de Peliculas')
    #Cambiamos el icono de la ventana
    #Se le debe pasar un argumento el cual es la ruta donde esta la imagen y debe ser .ico
    #La imagen esta en la carpeta img
    root.iconbitmap('img/cp-logo.ico')
    #Bloque la modificacion del tamaño de la ventana
    root.resizable(0,0)
    barra_menu(root)
    
    app = Frame(root= root)
    #El siguiente codigo es el paso a paso de crear un frame directamente en esta clase main
    """
        Creamos un frame
        Frame es el contenedor de los objetos y recibe un objeto tk
        frame = tk.Frame(root)
        #Y lo empaquetamos para que todos los componentes esten previamente cargados
        frame.pack()
        #Tamaño del frame pasandole los argumentos width y height y le damos un color con bg
        frame.config(width=480, height=320, bg='gray')
        
        En vez de eso creamos un paquete cliente donde estara un archivo init(vacio) y un archivo gui_app donde
        Estara toda la logica para crear un frame y despues importaremos esta clase
    """
    
    #Debe estar siempre al final, es como terminar el flujo de trabajo de tkinder
    app.mainloop() 
    
#Este es el entry point de la aplicacion
if __name__ == '__main__':
    main()
    
#NOTA: SI DESEAS EJECUTAR LA APLICACION DEBES HACERLO DESDE EL ENTORNO VIRTUAL