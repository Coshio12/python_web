#Interfaz de usuario de la aplicacion
#Importamos tkinder
import tkinter as tk

from tkinter import ttk

from model.pelicula_dao import crear_tabla,borrar_tabla

from model.pelicula_dao import Pelicula, guardar, listar,editar, eliminar

from tkinter import messagebox as mg

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
    menu_inicio.add_command(label='Crear Registro', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro', command=borrar_tabla)
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
        
        self.id_pelicula = None
        
        
        #Agregamos al constructor todo lo que tendra campos de peliculas
        self.campos_pelicula()
        
        #Agregamos el metodo de desabilitar los campos
        self.desabilitar_campos()
        
        self.tabla_peliculas()
        
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
        #Tambien hay que darle funcionalidad a los botones para ello cada que ejecutemos el boton cancelar o nuevo
        #tenemos que pasarle datos vacios para ello eusaremos el objeto StringVar en una nueva variable
        self.mi_nombre = tk.StringVar()
        #Y esta variable le pasamos como argumento cada que creemos el entry con textvariable
        #Y repetimos con los otros entrys
        self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)
        #Creamos la personalizacion delentry con el state de deshabilitado y personalizamos el estilo del texto
        self.entry_nombre.config(width=50, font= ('Arial',12))
        #Lo agregamos a la grid pero modificando la columna
        self.entry_nombre.grid(row=0, column=1,columnspan=2, padx= 10, pady= 10)
        #Este mismo proceso lo repetimos para los otros campos
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, font=('Arial',12))
        self.entry_duracion.grid(row=1, column=1,columnspan=2, padx=10, pady=10)
        
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self,textvariable=self.mi_genero)
        self.entry_genero.config(width=50, font=('Arial',12))
        self.entry_genero.grid(row=2, column=1,columnspan=2, padx=10, pady=10)
        
        #BOTONES DE GUARDAR, CANCELAR,NUEVO
        #NUEVO
        #Al ser el boton nuevo queremos que el usuario digite valores
        #entonces tenemos que habilitar los campos y para ello debemos agregar el parametro
        #command con el metodo para que se habiliten los campos
        self.boton_nuevo = tk.Button(self, text= 'NUEVO',command= self.habilidar_campos)
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
        #Al ser el boton guardar queremos que los entry esten vacios despues  de guardar la informacion
        #entonces tenemos que pasarle datos vacios y despues de guardar que se desabiliten los campos
        self.boton_guardar = tk.Button(self, text= 'GUARDAR',command=self.guardar_datos)
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
        #Al ser el boton cancelar queremos desabilitar los campos
        #Para ello debemos agregar el parametro command con el metodo para que se habiliten los campos
        self.boton_cancelar = tk.Button(self, text= 'CANCELAR',command=self.desabilitar_campos)
        self.boton_cancelar.config(
            width=20, 
            bg='#BD152E',
            font=('Time New Roman',12,'bold'),
            fg='white', 
            cursor='hand2',
            activebackground='#E15370'
            )
        self.boton_cancelar.grid(row=3,column=2, padx=10, pady=10)#Dibuja el boton
    
    #Creamos el metodo de habilitar campos
    def habilidar_campos(self):
        #Le pasamos a los campos datos vacios
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        #Y a los diferentes entrys le damos una funcionalidad que en este caso es cambiar el estado
        #como estamos habilitando, el state tiene que ser normal
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
    
    #Creamos el metodo de desahabilitar campos
    def desabilitar_campos(self):
        #Le pasamos a los campos datos vacios
        self.id_pelicula = None
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        #Y a los diferentes entrys le damos una funcionalidad que en este caso es cambiar el estado
        #como estamos desahabilitando, el state tiene que ser disabled
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    
    def guardar_datos(self):
        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get(),
        )
        if self.id_pelicula == None:
            
            guardar(pelicula)
        else:
            editar(pelicula,self.id_pelicula)
            
        self.tabla_peliculas()
        
        self.desabilitar_campos()
        
    def tabla_peliculas(self):
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()
        
        self.tabla = ttk.Treeview(self, 
            column= ('NOMBRE', 'DURACION','GENERO'))
        
        self.tabla.grid(row=4,column=0, columnspan=4)
        
        #Scrollbar para la tabla si exede 10 registros
        self.scroll = ttk.Scrollbar(self,
                orient='vertical',
                command=self.tabla.yview,
            )
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)
        
        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='NOMBRE')
        self.tabla.heading('#2',text='DURACION')
        self.tabla.heading('#3',text='GENERO')
        
        #iterar
        for p in self.lista_peliculas:
            self.tabla.insert('',0,text=p[0],
                values=(p[1],p[2],p[3]))
        
        self.boton_editar = tk.Button(self, text= 'EDITAR', command=self.editar_datos)
        self.boton_editar.config(
            width=20, 
            bg='green',
            font=('Time New Roman',12,'bold'),
            fg='white', 
            cursor='hand2',
            activebackground='#35BD6F'
            )
        self.boton_editar.grid(row=5,column=0, padx=10, pady=10)#Dibuja el boton
        
        self.boton_eliminar = tk.Button(self, text= 'ELIMINAR', command=self.eliminar_datos)
        self.boton_eliminar.config(
            width=20, 
            bg='#BD152E',
            font=('Time New Roman',12,'bold'),
            fg='white', 
            cursor='hand2',
            activebackground='#E15370'
            )
        self.boton_eliminar.grid(row=5,column=1, padx=10, pady=10)#Dibuja el boton
        
    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(
                self.tabla.selection()
            )['values'][0]
            
            self.duracion_pelicula = self.tabla.item(
                self.tabla.selection()
            )['values'][1]
            
            self.genero_pelicula = self.tabla.item(
                self.tabla.selection()
            )['values'][2]
            
            self.habilidar_campos()
            
            self.entry_nombre.insert(0,self.nombre_pelicula)
            self.entry_duracion.insert(0,self.duracion_pelicula)
            self.entry_genero.insert(0,self.genero_pelicula)
        except:
            titulo = 'Edicion de datos'
            mensaje = 'No se ha seleccionado ningun registro'
            mg.showerror(titulo,mensaje)
            
    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_pelicula)
            
            self.tabla_peliculas()
            
            self.id_pelicula = None
        except:
            titulo = 'Eliminacion de datos'
            mensaje = 'No se ha seleccionado ningun registro'
            mg.showerror(titulo,mensaje)
            
    