#Interfaz de usuario de la aplicacion
#Importamos tkinder
import tkinter as tk

#Creamos una barra de menu que reciba la raiz
def barra_menu(root):
    #Creamos un objeto de menu que recibe la riaz
    barra_menu = tk.Menu(root)
    #Realizamos la personalizacion del menu
    root.config(menu = barra_menu, width = 300, height = 300)
    
    #Creamos un objeto de menu_inicio que recibe la barra_menu y un tearoff para que no aparezca saltos de linea
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    #Agreamos a la barra en forma de cascada el label de como se llamara el primer componente del menu
    #En este caso se llamara inicio, y se creara el menu despegable de inicio
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)
    
    #Añadimos componentes al menu despegable de inicio con add_command
    menu_inicio.add_command(label='Crear Registro')
    menu_inicio.add_command(label='Eliminar Registro')
    #A este ultimo que es salir le damos la funcionalidad de destroy
    #Esto hara que se cierre la ventana
    menu_inicio.add_command(label='Salir', command = root.destroy)
    
    #Si queremos agregar mas componentes a la barra de menu simplemente los añadimos con la cascada
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')
    

#Creamos una clase frame que herede los metodos de frame
class Frame(tk.Frame):
    #Creamos el constructor que recibira la raiz que de momento esta vacia
    def __init__(self, root = None):
        #heredamos los metodos y pasamos ciertas modificaciones que querramos hacer para el config del frame
        super().__init__(root,width=480, height=320)
        #Asignamos los valores
        self.root = root
        #Lo empaquetamos
        self.pack()
        #Configuramos y modificamos el frame, en este caso solamente de damos un color
        #self.config( bg='gray')
        
        #Agregamos al constructor todo lo que tendra campos de peliculas
        self.campos_pelicula()
        
    #Labels de campos de pelicula
    def campos_pelicula(self):
        #Labels de cada campo
        self.label_nombre = tk.Label(self, text = 'NOMBRE DE LA PELICULA: ')
        #Configuramos el label dandole los estilos que querramos
        #En este ejemplo en config le pasamos el font y como font puede ser tanto el tipo de letra como la escritura
        #Podemos pasarle la informacion en parentesis, siendo letra Arial, tamaño 12 y en negrilla
        self.label_nombre.config(font= ('Arial',12,'bold'))
        #Tenemos que posiciar los labels dentro del frame
        #Para ello usamos los grid que trabajan en columnas y filas
        #Y tambien para que no esten totalmente juntos usamos los estilos de padding en x y y para generar un espacio entre componentes
        self.label_nombre.grid(row=0, column=0, padx=10,pady=10)
        
        #Siguiendo la logica anterior creamos otros dos labels
        self.label_duracion = tk.Label(self, text = 'DURACION DE LA PELICULA: ')
        self.label_duracion.config(font= ('Arial',12,'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10,pady=10)

        
        self.label_genero = tk.Label(self, text = 'GENERO DE LA PELICULA: ')
        self.label_genero.config(font= ('Arial',12,'bold'))
        self.label_genero.grid(row=2, column=0, padx=10,pady=10)
        
        #Entrys, campos de entrada de la informacion
        #Creamos un objeto del tipo entry con el self ya que esta en una clase frame
        self.entry_nombre = tk.Entry(self)
        #Creamos la personalizacion delentry con el state de deshabilitado y personalizamos el estilo del texto
        self.entry_nombre.config(width=50, state='disabled', font= ('Arial',12))
        #Lo agregamos a la grid pero modificando la columna
        self.entry_nombre.grid(row=0, column=1,columnspan=2, padx= 10, pady= 10)
        #Este mismo proceso lo repetimos para los otros campos
        
        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50, state='disabled', font=('Arial',12))
        self.entry_duracion.grid(row=1, column=1,columnspan=2, padx=10, pady=10)
        
        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50, state='disabled', font=('Arial',12))
        self.entry_genero.grid(row=2, column=1,columnspan=2, padx=10, pady=10)
        
        #BOTONES DE GUARDAR, CANCELAR,NUEVO
        #NUEVO
        self.boton_nuevo = tk.Button(self, text= 'NUEVO')
        self.boton_nuevo.config(
            width=20, 
            bg='green',
            font=('Time New Roman',12,'bold'),
            fg='white', 
            cursor='hand2',
            activebackground='#35BD6F'
            )
        self.boton_nuevo.grid(row=3,column=0, padx=10, pady=10)#Dibuja el boton
        
        #GUARDAR
        self.boton_guardar = tk.Button(self, text= 'GUARDAR')
        self.boton_guardar.config(
            width=20, 
            bg='#1658A2',
            font=('Time New Roman',12,'bold'),
            fg='white', 
            cursor='hand2',
            activebackground='#3586DF'
            )
        self.boton_guardar.grid(row=3,column=1, padx=10, pady=10)#Dibuja el boton
        
        #CANCELAR
        self.boton_cancelar = tk.Button(self, text= 'CANCELAR')
        self.boton_cancelar.config(
            width=20, 
            bg='#BD152E',
            font=('Time New Roman',12,'bold'),
            fg='white', 
            cursor='hand2',
            activebackground='#E15370'
            )
        self.boton_cancelar.grid(row=3,column=2, padx=10, pady=10)#Dibuja el boton
        
        